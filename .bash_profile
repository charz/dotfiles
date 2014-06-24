
if [ -f ~/.prompt ]; then
    . ~/.prompt
fi

export PATH=/usr/local/bin:/usr/local/sbin:$PATH
export WORKON_HOME=$HOME/.VENV
source /usr/local/bin/virtualenvwrapper.sh
