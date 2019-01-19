PROMPT_COMMAND='$(echo $LINE_NUM $(fc -l|tail -1|awk '\''{for (i=2; i<NF; i++) printf $i " "; print $NF}'\'') >> $LOGFILE.hist);LINE_NUM=$(($LINE_NUM+1))'
LINE_NUM=0
AUDIT_FOLDER=$(dirname $(dirname $BASH_SOURCE))
AUDIT_NAME=$(basename $AUDIT_FOLDER)
PS1='\n\033[32;1m\u@\h\033[0m:\033[34;1m\W\033[0m [IP: \033[0;1m`ip route get 1 2>/dev/null|sed -n 1p|cut -f7 -d" "`]\033[0m `date +"%D-%T"`\n[$LINE_NUM] \$ '

if [ "$(ps -ocommand= -p $PPID | awk '{print $1}')" != 'script' ];
then
    export LOGFILE="$AUDIT_FOLDER/logs/shell/$(date +%Y-%m-%d__%H-%M-%S)_$(dd if=/dev/urandom bs=1 count=20 2>/dev/null|base64|tr -dc 'a-zA-Z0-9'|fold -w 8|head -n1)_shell.log"
    exec script -q -f "$LOGFILE";
fi

echo -e "\x1b[32mLogging to $LOGFILE"
echo -e "Stop with : audit.py stop $AUDIT_NAME\x1b[0m"
