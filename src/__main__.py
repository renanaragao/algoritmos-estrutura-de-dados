#!/usr/bin/env python3

import sys

from simple_term_menu import TerminalMenu

from sort.bubblesort import bubblesort
from sort.quicksort import quicksort
from sort.heapsort import BinaryHeap

actions = {0: bubblesort, 1: quicksort}


def main():
    options = ["bubblesort", "quicksort", "heapsort"]
    terminal_menu = TerminalMenu(options)

    index = terminal_menu.show()

    if index in actions:
        print(actions[index]([8, 5, 10, 6, 8]))

    heap = BinaryHeap()

    values = [4, 2, 8, 7, 1, 5, 3, 6, 10]

    for value in values:
        heap.insert(value)

    print(heap._data)

    print(heap.dequeue())
    print(heap.dequeue())
    print(heap.dequeue())
    print(heap.dequeue())
    print(heap.dequeue())
    print(heap.dequeue())
    print(heap.dequeue())
    print(heap.dequeue()) 

    print(BinaryHeap.heapSort(values))


if __name__ == "__main__":
    sys.exit(main())
