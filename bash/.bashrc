#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

export PS1='$(git branch &>/dev/null; if [ $? -eq 0 ]; then \
echo "\[\e[1m\]\u@\h\[\e[0m\]: \w [\[\e[34m\]$(git branch | grep ^* | sed s/\*\ //)\[\e[0m\]\
$(echo `git status` | grep "nothing to commit" > /dev/null 2>&1; if [ "$?" -ne "0" ]; then \
echo "\[\e[1;31m\]*\[\e[0m\]"; fi)] \$ "; else \
echo "\[\e[1m\]\u@\h\[\e[0m\]: \w \$ "; fi )'

#ignore upper and lowercase when TAB completion
bind "set completion-ignore-case on"

#list
alias ls='ls --color=auto'
alias la='ls -a'
alias ll='ls -la'
alias l.="ls -A | egrep '^\.'"

#clear
alias c="clear"

# tty-clock
alias cl="tty-clock -s -S -c -C 7 -D"

#git
alias ga="git add"
alias gc="git commit -m"
alias gp="git push origin main"

#fix obvious typo's
alias cd..='cd ..'
alias pdw="pwd"
alias udpate='sudo pacman -Syu'
alias upate='sudo pacman -Syu'
alias updte='sudo pacman -Syu'
alias updqte='sudo pacman -Syu'
alias upqll="yay -Syu --noconfirm"
alias upal="yay -Syu --noconfirm"

#quickly kill conkies
alias kc='killall conky'

#hardware info --short
alias hw="hwinfo --short"

#Cleanup orphaned packages
alias cleanup='sudo pacman -Rns $(pacman -Qtdq)'

#shutdown or reboot
alias ssn="sudo shutdown now"
alias sr="sudo reboot"

# # ex = EXtractor for all kinds of archives
# # usage: ex <file>
ex ()
{
  if [ -f $1 ] ; then
    case $1 in
      *.tar.bz2)   tar xjf $1   ;;
      *.tar.gz)    tar xzf $1   ;;
      *.bz2)       bunzip2 $1   ;;
      *.rar)       unrar x $1   ;;
      *.gz)        gunzip $1    ;;
      *.tar)       tar xf $1    ;;
      *.tbz2)      tar xjf $1   ;;
      *.tgz)       tar xzf $1   ;;
      *.zip)       unzip $1     ;;
      *.Z)         uncompress $1;;
      *.7z)        7z x $1      ;;
      *.deb)       ar x $1      ;;
      *.tar.xz)    tar xf $1    ;;
      *.tar.zst)   unzstd $1    ;;
      *)           echo "'$1' cannot be extracted via ex()" ;;
    esac
  else
    echo "'$1' is not a valid file"
  fi
}
