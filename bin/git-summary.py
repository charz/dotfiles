#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess


def read_pipe_lines(c):
    expand = isinstance(c, basestring)
    p = subprocess.Popen(c, stdout=subprocess.PIPE, shell=expand)
    pipe = p.stdout
    val = pipe.readlines()
    if pipe.close() or p.wait():
        raise Exception('Command failed: %s' % str(c))

    return val


def main():
    print '%-20s\t%10s\t%10s\t%10s\t%10s\t%10s\t%10s' % ('Author', 'Commits',
                                                         'Insert', 'Delete',
                                                         'Avg. Ins',
                                                         'Avg. Del',
                                                         '%')

    print '{0}\t{1}\t{1}\t{1}\t{1}\t{1}\t{1}'.format('='*20, '='*10)

    cmd = 'git shortlog -s -n'
    lines = read_pipe_lines(cmd)
    for l in lines:
        try:
            commits, author = l.split('\t')
            commits = int(commits)
            author = author.strip()
            gitcmd = 'git log --numstat --pretty=%%H --author="%s"' % author
            git_lines = read_pipe_lines(gitcmd)
            inserted = deleted = 0
            for nl in git_lines:
                try:
                    val = nl.split('\t')
                    if len(val) > 2:
                        inserted = inserted + int(val[0])
                        deleted = deleted + int(val[1])
                except:
                    pass

            percentage = (float(deleted)/float(inserted)) * 100.0
            print '%-20s\t%10d\t%10d+\t%10d' \
                  '-\t%10d+\t%10d-\t%10d' % (author, commits,
                                             inserted, deleted,
                                             (inserted/commits),
                                             (deleted/commits),
                                             percentage,
                                             )
        except Exception as e:
            print 'Get author fail! %s' % e
            pass

if __name__ == '__main__':
    main()
