#!/usr/bin/env python3

import sys
from simple_term_menu import TerminalMenu
from sort.bubblesort import bubblesort

actions = {0: bubblesort}


def main():
    options = ["bubblesort"]
    terminal_menu = TerminalMenu(options)

    menu_entry_index = terminal_menu.show()
    print(actions[menu_entry_index]([7, 5, 10, 6, 8]))


if __name__ == "__main__":
    sys.exit(main())
