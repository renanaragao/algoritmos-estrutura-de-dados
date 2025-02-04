#!/usr/bin/env python3

import sys
from simple_term_menu import TerminalMenu
from sort.quicksort import quicksort
from sort.bubblesort import bubblesort

actions = {0: bubblesort, 1: quicksort}


def main():
    options = ["bubblesort", "quicksort"]
    terminal_menu = TerminalMenu(options)

    index = terminal_menu.show()
    print(actions[index]([7, 5, 10, 6, 8]))


if __name__ == "__main__":
    sys.exit(main())
