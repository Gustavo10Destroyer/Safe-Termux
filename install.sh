#!/data/data/com.termux/files/usr/bin/bash

YAN="\x1b[1;36m"
GREEN="\x1b[1;32m"
YELLOW="\x1b[1;33m"
RESET="\x1b[0m"

if [ -d "$HOME/Safe-Termux" ]; then
    echo -e "${CYAN}[${YELLOW}!${CYAN}] O '${GREEN}Safe-Termux${CYAN}' está instalado!${RESET}"
    printf "${CYAN}[${YELLOW}!${CYAN}] Deseja re-instalar o '${GREEN}Safe-Termux${CYAN}'? [${GREEN}s${CYAN}/${YELLOW}N${CYAN}]: ${RESET}"
    read -r remove

    if [[ "$remove" == "S" || "$remove" == "s" || "$remove" == "Sim" || "$remove" == "sim" || "$remove" == "sIm" || "$remove" == "SiM" || "$remove" == "siM" || "$remove" == "SIm" ]]; then
        rm -rf "$HOME/Safe-Termux"
    else
        exit 0
    fi
fi

cd $HOME
git clone https://github.com/Imperador-RIC/Safe-Termux
cd Safe-Termux/source
python "install.py"
clear

echo -e "${CYAN}[${YELLOW}!${CYAN}] O '${GREEN}Safe-Termux${CYAN}' foi instalado!${RESET}"
