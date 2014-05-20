#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess

def read_pipe_lines(c):
    expand = isinstance(c, basestring)
    p = subprocess.Popen(c, stdout=subprocess.PIPE, shell=expand)
    pipe = p.stdout
    val = pipe.readlines()
    if pipe.close() or p.wait():
        die('Command failed: %s' % str(c))

    return val


def main():
    print '%-20s\t%10s\t%10s\t%10s\t%10s\t%10s'% ('Author', 'Commits',
                                                'Insert', 'Delete',
                                                'Avg. Ins', 'Avg. Del')

    print '{0}\t{1}\t{1}\t{1}\t{1}\t{1}'.format('='*20, '='*10)

    cmd = 'git shortlog -s -n'
    lines = read_pipe_lines(cmd)
    for l in lines:
        try:
            commits = int(l.split('\t')[0].strip())
            author = l.split('\t')[1].strip()
            gitcmd = 'git log --numstat --pretty=%%H --author="%s"'% author
            git_lines = read_pipe_lines(gitcmd)
            inserted = 0
            deleted = 0
            for nl in git_lines:
                try:
                    val = nl.split('\t')
                    if len(val) > 2:
                        inserted = inserted + int(val[0])
                        deleted = deleted + int(val[1])
                except:
                    pass

            print '%-20s\t%10d\t%10d+\t%10d-\t%10d+\t%10d-'% (author, commits,
                                                            inserted, deleted,
                                                            (inserted/commits),(deleted/commits))

        except Exception as e:
            print 'Get author fail! %s'% l
            pass
    

if __name__ == '__main__':
    main()
