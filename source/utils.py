import re
import os
import sys

def parse(command: str) -> str:
    # replace all environment variables
    command = re.sub(r"\$([a-zA-Z0-9_]+)", lambda match: os.environ.get(match.group(1), ""), command)

    return command

# escreve no centro da tela
# centralizando o texto na horizontal e vertical
def print_centered(text: str) -> None:
    rows, columns = os.get_terminal_size()

    # centralizando o texto na vertical
    text = text.splitlines()

    y = (columns - len(text)) // 2

    for index, line in enumerate(text):
        # centralizando o texto na horizontal
        fake_line = re.sub(r"\x1b\[[0-9;]*m", "", line)
        x = (rows - len(fake_line)) // 2

        sys.stdout.write("\x1b[{};{}H".format(y + index, x))
        sys.stdout.write(line)
        sys.stdout.write("\n")

    sys.stdout.flush()