def selectionsort(arr, verbose=True):
    """
    Implementação do Selection Sort com prints explicativos.
    
    Args:
        arr: Lista a ser ordenada
        verbose: Se True, exibe prints detalhados do processo
    
    Returns:
        Lista ordenada
    """
    if verbose:
        print(f"\n{'='*60}")
        print(f"🎯 SELECTION SORT - ORDENAÇÃO POR SELEÇÃO")
        print(f"{'='*60}")
        print(f"Array inicial: {arr}")
        print(f"Tamanho: {len(arr)}")
        print(f"\n💡 Conceito: Encontra o menor elemento e coloca na posição")
        print(f"   correta, repetindo até ordenar todo o array.")
        print(f"{'='*60}")
    
    length = len(arr)
    total_comparisons = 0
    total_swaps = 0
    
    for i in range(length - 1):
        # Assume que o primeiro elemento não ordenado é o menor
        min_index = i
        
        if verbose:
            print(f"\n{'─'*60}")
            print(f"🔄 PASSAGEM {i + 1}/{length - 1}")
            print(f"{'─'*60}")
            if i > 0:
                print(f"   ✅ Primeiros {i} elemento(s) já ordenado(s)")
            print(f"   🔍 Procurando o menor elemento de {i} até {length - 1}")
            print(f"   Assumindo inicialmente que o menor é arr[{i}]={arr[i]}")
        
        # Procura o menor elemento no restante do array
        for j in range(i + 1, length):
            total_comparisons += 1
            
            if verbose:
                # Visualização do array
                visual = []
                for k in range(length):
                    if k < i:
                        visual.append(f"✓{arr[k]}")  # Já ordenados
                    elif k == i:
                        visual.append(f"[{arr[k]}]")  # Posição atual
                    elif k == min_index:
                        visual.append(f"🔹{arr[k]}")  # Menor encontrado até agora
                    elif k == j:
                        visual.append(f"👉{arr[k]}")  # Comparando agora
                    else:
                        visual.append(f" {arr[k]} ")
                
                print(f"\n   Comparando: arr[{j}]={arr[j]} com menor atual arr[{min_index}]={arr[min_index]}")
                print(f"   Estado: {' '.join(visual)}")
            
            if arr[j] < arr[min_index]:
                if verbose:
                    print(f"   🆕 NOVO MENOR! {arr[j]} < {arr[min_index]} → Atualizando min_index para {j}")
                min_index = j
            else:
                if verbose:
                    print(f"   ✓ {arr[j]} >= {arr[min_index]} → Menor continua sendo arr[{min_index}]={arr[min_index]}")
        
        # Troca o menor elemento encontrado com a posição atual
        if min_index != i:
            if verbose:
                print(f"\n   🔀 TROCA: arr[{i}]={arr[i]} ↔ arr[{min_index}]={arr[min_index]}")
            
            arr[i], arr[min_index] = arr[min_index], arr[i]
            total_swaps += 1
            
            if verbose:
                print(f"   Resultado: {arr}")
        else:
            if verbose:
                print(f"\n   ✓ Elemento arr[{i}]={arr[i]} já está na posição correta!")
        
        if verbose:
            print(f"\n   📊 Fim da passagem {i + 1}")
            print(f"   Array atual: {arr}")
    
    if verbose:
        print(f"\n{'='*60}")
        print(f"✅ ORDENAÇÃO CONCLUÍDA!")
        print(f"{'='*60}")
        print(f"Array final: {arr}")
        print(f"Total de comparações: {total_comparisons}")
        print(f"Total de trocas: {total_swaps}")
        print(f"{'='*60}\n")
    
    return arr


# Exemplo de uso
if __name__ == "__main__":
    print("=" * 60)
    print("DEMONSTRAÇÃO DO SELECTION SORT")
    print("=" * 60)
    
    # Teste 1: Array desordenado
    print("\n🔹 TESTE 1: Array completamente desordenado")
    arr1 = [64, 25, 12, 22, 11]
    resultado1 = selectionsort(arr1.copy())
    
    # Teste 2: Array já ordenado
    print("\n🔹 TESTE 2: Array já ordenado")
    arr2 = [1, 2, 3, 4, 5]
    resultado2 = selectionsort(arr2.copy())
    
    # Teste 3: Array pequeno
    print("\n🔹 TESTE 3: Array pequeno")
    arr3 = [8, 5, 10]
    resultado3 = selectionsort(arr3.copy())
    
    # Teste 4: Array com valores repetidos
    print("\n🔹 TESTE 4: Array com valores repetidos")
    arr4 = [5, 2, 8, 2, 9]
    resultado4 = selectionsort(arr4.copy())
