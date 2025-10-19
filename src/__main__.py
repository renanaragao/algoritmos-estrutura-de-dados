#!/usr/bin/env python3

import sys

from simple_term_menu import TerminalMenu

from sort.bubblesort import bubblesort
from sort.quicksort import quicksort
from sort.heapsort import BinaryHeap
from sort.selectionsort import selectionsort
from sort.mergesort import mergesort
from search.binarysearch import binary_search, binary_search_recursive


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


def run_sorting_demo(algorithm_name, algorithm_func):
    """Demonstração de algoritmos de ordenação"""
    print(f"\n{'='*60}")
    print(f"DEMONSTRAÇÃO DE {algorithm_name.upper()}")
    print(f"{'='*60}")
    
    try:
        print("\nEscolha uma opção:")
        print("1. Array de exemplo")
        print("2. Digitar array personalizado")
        
        choice = input("\nOpção (1 ou 2): ").strip()
        
        if choice == "1":
            arr = [64, 34, 25, 12, 22, 11, 90]
        elif choice == "2":
            arr_input = input("\nDigite os números separados por espaço: ")
            arr = [int(x) for x in arr_input.split()]
        else:
            print("❌ Opção inválida!")
            input("\nPressione ENTER para continuar...")
            return
        
        print(f"\nArray original: {arr}")
        resultado = algorithm_func(arr.copy(), verbose=True)
        
    except ValueError:
        print("\n❌ Erro: Digite apenas números válidos!")
    except Exception as e:
        print(f"\n❌ Erro: {e}")
    
    input("\nPressione ENTER para continuar...")


def run_heapsort_demo():
    """Demonstração específica do Heap Sort"""
    print(f"\n{'='*60}")
    print(f"DEMONSTRAÇÃO DE HEAP SORT")
    print(f"{'='*60}")
    
    print("\nEscolha uma opção:")
    print("1. Heap Sort (ordenação)")
    print("2. Binary Heap (inserções e remoções)")
    
    choice = input("\nOpção (1 ou 2): ").strip()
    
    if choice == "1":
        try:
            print("\nEscolha:")
            print("1. Array de exemplo")
            print("2. Digitar array personalizado")
            
            arr_choice = input("\nOpção (1 ou 2): ").strip()
            
            if arr_choice == "1":
                arr = [4, 10, 3, 5, 1, 8, 2, 7]
            elif arr_choice == "2":
                arr_input = input("\nDigite os números separados por espaço: ")
                arr = [int(x) for x in arr_input.split()]
            else:
                print("❌ Opção inválida!")
                input("\nPressione ENTER para continuar...")
                return
            
            print(f"\nArray original: {arr}")
            resultado = BinaryHeap.heapSort(arr.copy(), verbose=True)
            
        except ValueError:
            print("\n❌ Erro: Digite apenas números válidos!")
        except Exception as e:
            print(f"\n❌ Erro: {e}")
    
    elif choice == "2":
        heap = BinaryHeap(verbose=True)
        
        try:
            values_input = input("\nDigite os números a inserir (separados por espaço): ")
            values = [int(x) for x in values_input.split()]
            
            for value in values:
                heap.insert(value)
            
            print("\n" + "="*60)
            print("Removendo elementos do heap (em ordem decrescente):")
            print("="*60)
            
            while len(heap._data) > 0:
                removed = heap.dequeue()
        
        except ValueError:
            print("\n❌ Erro: Digite apenas números válidos!")
        except Exception as e:
            print(f"\n❌ Erro: {e}")
    else:
        print("❌ Opção inválida!")
    
    input("\nPressione ENTER para continuar...")


def main():
    options = ["bubblesort", "quicksort", "heapsort", "selectionsort", "mergesort", "binarysearch"]
    terminal_menu = TerminalMenu(options)

    index = terminal_menu.show()

    if index == 0:  # bubblesort
        run_sorting_demo("bubblesort", bubblesort)
    elif index == 1:  # quicksort
        run_sorting_demo("quicksort", quicksort)
    elif index == 2:  # heapsort
        run_heapsort_demo()
    elif index == 3:  # selectionsort
        run_sorting_demo("selectionsort", selectionsort)
    elif index == 4:  # mergesort
        run_sorting_demo("mergesort", mergesort)
    elif index == 5:  # binarysearch
        run_binary_search()


if __name__ == "__main__":
    sys.exit(main())
