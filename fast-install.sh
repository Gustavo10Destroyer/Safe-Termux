#!/data/data/com.termux/files/usr/bin/bash

cd $HOME

if [ -d "$HOME/Safe-Termux" ]; then
    rm -rf Safe-Termux .bloqueio
fi

git clone https://github.com/Imperador-RIC/Safe-Termux
cd Safe-Termux/source
python3 install.py

clear
echo "O Safe-Termux foi instalado com sucesso!"
