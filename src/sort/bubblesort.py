def bubblesort(arr, verbose=True):
    """
    Implementação do Bubble Sort com prints explicativos.
    
    Args:
        arr: Lista a ser ordenada
        verbose: Se True, exibe prints detalhados do processo
    
    Returns:
        Lista ordenada
    """
    if verbose:
        print(f"\n{'='*60}")
        print(f"🫧 BUBBLE SORT - ORDENAÇÃO POR BOLHA")
        print(f"{'='*60}")
        print(f"Array inicial: {arr}")
        print(f"Tamanho: {len(arr)}")
        print(f"\n💡 Conceito: Compara elementos adjacentes e os troca se")
        print(f"   estiverem na ordem errada. O maior 'borbulha' para o fim.")
        print(f"{'='*60}")
    
    length = len(arr)
    total_comparisons = 0
    total_swaps = 0
    
    for i in range(length):
        changes = 0
        
        if verbose:
            print(f"\n{'─'*60}")
            print(f"🔄 PASSAGEM {i + 1}/{length}")
            print(f"{'─'*60}")
            print(f"   Área não ordenada: 0 até {length - i - 1}")
            if i > 0:
                print(f"   ✅ Últimos {i} elemento(s) já ordenado(s)")
        
        for j in range(0, length - i - 1):
            total_comparisons += 1
            
            if verbose:
                # Visualização do array com destaque nos elementos sendo comparados
                visual = []
                for k in range(length):
                    if k == j:
                        visual.append(f"[{arr[k]}]")
                    elif k == j + 1:
                        visual.append(f"[{arr[k]}]")
                    elif k >= length - i:
                        visual.append(f"✓{arr[k]}")  # Já ordenados
                    else:
                        visual.append(f" {arr[k]} ")
                
                print(f"\n   Comparando: arr[{j}]={arr[j]} com arr[{j+1}]={arr[j + 1]}")
                print(f"   Estado: {' '.join(visual)}")
            
            if arr[j] > arr[j + 1]:
                if verbose:
                    print(f"   🔀 TROCA! {arr[j]} > {arr[j + 1]} → Trocando posições")
                
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                changes += 1
                total_swaps += 1
                
                if verbose:
                    print(f"   Resultado: {arr}")
            else:
                if verbose:
                    print(f"   ✓ OK! {arr[j]} <= {arr[j + 1]} → Mantém ordem")
        
        if verbose:
            print(f"\n   📊 Fim da passagem {i + 1}: {changes} troca(s) realizada(s)")
            print(f"   Array atual: {arr}")
        
        # Otimização: se não houve trocas, o array já está ordenado
        if changes == 0:
            if verbose:
                print(f"\n   🎉 OTIMIZAÇÃO: Nenhuma troca necessária!")
                print(f"   O array já está ordenado. Finalizando...")
            break
    
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
    print("DEMONSTRAÇÃO DO BUBBLE SORT")
    print("=" * 60)
    
    # Teste 1: Array desordenado
    print("\n🔹 TESTE 1: Array completamente desordenado")
    arr1 = [64, 34, 25, 12, 22, 11, 90]
    resultado1 = bubblesort(arr1.copy())
    
    # Teste 2: Array quase ordenado (melhor caso)
    print("\n🔹 TESTE 2: Array quase ordenado")
    arr2 = [1, 2, 3, 5, 4, 6]
    resultado2 = bubblesort(arr2.copy())
    
    # Teste 3: Array pequeno
    print("\n🔹 TESTE 3: Array pequeno")
    arr3 = [8, 5, 10]
    resultado3 = bubblesort(arr3.copy())
