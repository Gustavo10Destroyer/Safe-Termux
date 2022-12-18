#!/data/data/com.termux/files/usr/bin/bash

cd $HOME

if [ -d "$HOME/Safe-Termux" ]; then
    echo "[!] O 'Safe-Termux' já está instalado!"
    echo "[*] Re-instalando o 'Safe-Termux'..."

    python3 $HOME/Safe-Termux/source/uninstall.py
    rm -rf $HOME/Safe-Termux
else
    echo "[*] Instalando o 'Safe-Termux'..."
fi

git clone https://github.com/Gustavo10Destroyer/Safe-Termux
cd Safe-Termux/source
python3 install.py
clear

echo "[*] O 'Safe-Termux' foi instalado com sucesso!"