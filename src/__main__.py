#!/usr/bin/env python3

import sys

from simple_term_menu import TerminalMenu

from sort.bubblesort import bubblesort
from sort.quicksort import quicksort
from sort.heapsort import BinaryHeap
from search.binarysearch import binary_search, binary_search_recursive

actions = {0: bubblesort, 1: quicksort}


def run_binary_search():
    """Demonstração da busca binária"""
    print("\n" + "="*60)
    print("DEMONSTRAÇÃO DE BUSCA BINÁRIA")
    print("="*60)
    
    # Array ordenado para busca
    array = [2, 5, 8, 12, 16, 23, 38, 45, 56, 67, 78]
    
    print("\n🔹 Escolha o tipo de busca:")
    search_options = ["Busca Iterativa", "Busca Recursiva", "Voltar"]
    search_menu = TerminalMenu(search_options)
    search_choice = search_menu.show()
    
    if search_choice == 2:  # Voltar
        return
    
    print(f"\nArray ordenado: {array}")
    try:
        target = int(input("\nDigite o número que deseja buscar: "))
        
        if search_choice == 0:  # Iterativa
            resultado = binary_search(array, target)
        else:  # Recursiva
            resultado = binary_search_recursive(array, target)
        
        if resultado != -1:
            print(f"\n✅ Resultado final: Elemento {target} encontrado no índice {resultado}")
        else:
            print(f"\n❌ Resultado final: Elemento {target} não encontrado no array")
            
    except ValueError:
        print("\n❌ Erro: Digite um número válido!")
    
    input("\nPressione ENTER para continuar...")


def main():
    options = ["bubblesort", "quicksort", "heapsort", "binarysearch"]
    terminal_menu = TerminalMenu(options)

    index = terminal_menu.show()

    if index in actions:
        print(actions[index]([8, 5, 10, 6, 8]))
    elif index == 3:  # binarysearch
        run_binary_search()

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
