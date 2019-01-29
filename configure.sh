#!/bin/bash

DIR="$(cd "$(dirname "$0")" && pwd)"
echo alias dlab="$DIR/dlab" >> /home/$USER/.bashrc
echo "[*]OK"
