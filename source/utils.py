import re
import os
import sys

def parse(command: str) -> str:
    # replace all environment variables
    command = re.sub(r"\$([a-zA-Z0-9_]+)", lambda match: os.environ.get(match.group(1), ""), command)

    return command

def print_centered(text: str) -> None:
    rows = 0
    columns = 0

    width, height = os.get_terminal_size()

    for line in text.splitlines():
        rows += 1
        # tamanho total é apenas números, letras e espaços
        total_size = re.sub(r"\x1b\[[0-9;]*m", "", line)

        columns = max(columns, len(total_size))

    line_index = 0
    width = round(width / 2)
    height = round((height - rows) / 2)

    if height % 2 != 0:
        line_index = 1

    for line in text.splitlines():
        x = width - round(len(line) / 2)
        y = height - round(round(rows / 2) / 2) + line_index

        sys.stdout.write("\033[{};{}H".format(height + line_index, x))
        sys.stdout.write(line + "\n")

        line_index += 1

    sys.stdout.flush()