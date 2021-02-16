#!/bin/bash

echo Creating symlinks...

# lightdm
ln -sf /~/dotfiles/lightdm/lightdm.conf /etc/lightdm/lightdm.conf

# qtile
ln -sf ~/dotfiles/qtile/config.py ~/.config/qtile

# bash
ln -sf ~/dotfiles/bash/.bashrc ~/

# alacritty
mkdir -p ~/.config/alacritty
ln -s ~/dotfiles/alacritty/alacritty.yml ~/.config/alacritty

# vim
ln -sf ~/dotfiles/vim/.vimrc ~/

# redshift
ln -sf ~/dotfiles/redshift/redshift.conf ~/.config

# neofetch
ln -sf ~/dotfiles/neofetch/config.conf ~/.config/neofetch

echo Done!