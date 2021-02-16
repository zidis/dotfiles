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

#cleanup orphaned packages
alias cleanup='sudo pacman -Rns $(pacman -Qtdq)'

#shutdown or reboot
alias ssn="sudo shutdown now"
alias sr="sudo reboot"

#scripts
alias roll="bash ~/dotfiles/scripts/roll.sh"
alias currency="bash ~/dotfiles/scripts/currency.sh"