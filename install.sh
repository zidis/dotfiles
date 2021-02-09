#!/bin/bash

# packages
echo Installing packages...

# redshift
pacman -S redshift

# tty-clock
yay -S tty-clock

# symlinks
echo Creating symlinks...

# qtile
ln -s /home/zidis/dotfiles/qtile/config.py /home/zidis/.config/qtile

# bash
ln -s /home/zidis/dotfiles/bash/.bashrc /home/zidis

# alacritty
mkdir -p /home/zidis/.config/test
ln -s /home/zidis/dotfiles/alacritty/alacritty.yml /home/zidis/.config/alacritty

# vim
ln -s /home/zidis/dotfiles/vim/.vimrc /home/zidis

# redshift
ln -s /home/zidis/dotfiles/redshift/redshift.conf /home/zidis/.config

# neofetch
ln -s /home/zidis/dotfiles/neofetch/config.conf /home/zidis/.config/neofetch

echo Done!