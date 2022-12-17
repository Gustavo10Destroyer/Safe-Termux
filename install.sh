CYAN="\x1b[1;36m"
GREEN="\x1b[1;32m"
YELLOW="\x1b[1;33m"
RESET="\x1b[0m"

cd $HOME
git clone https://github.com/Imperador-RIC/Safe-Termux
cd Safe-Termux/source
python "install.py"
clear

echo -e "${CYAN}[${YELLOW}!${CYAN}] O '${GREEN}Safe-Termux${CYAN}' foi instalado!${RESET}"
