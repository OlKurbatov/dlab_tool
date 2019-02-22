#!/bin/bash
#echo Attention! This script should run with SUDO privileges

#docker section
#groupadd docker
#usermod -aG docker $USER

DIR="$(cd "$(dirname "$0")" && pwd)"
echo alias dlab="$DIR/dlab" >> /home/$USER/.bashrc
echo "[*]OK"
echo "[!]Plese, re-login to your current session"
