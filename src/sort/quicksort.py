def quicksort(arr, start_pos=None, end_pos=None, verbose=True, depth=0):
    """
    Implementação do Quick Sort com prints explicativos.
    
    Args:
        arr: Lista a ser ordenada
        start_pos: Posição inicial do subarray
        end_pos: Posição final do subarray
        verbose: Se True, exibe prints detalhados do processo
        depth: Profundidade da recursão (para indentação)
    
    Returns:
        Lista ordenada
    """
    # Inicialização na primeira chamada
    if start_pos is None and end_pos is None:
        if verbose:
            print(f"\n{'='*60}")
            print(f"⚡ QUICK SORT - ORDENAÇÃO RÁPIDA")
            print(f"{'='*60}")
            print(f"Array inicial: {arr}")
            print(f"Tamanho: {len(arr)}")
            print(f"\n💡 Conceito: Divide o array usando um pivô, colocando")
            print(f"   elementos menores à esquerda e maiores à direita.")
            print(f"{'='*60}")
        start_pos = 0
        end_pos = len(arr) - 1
    
    # ponteiro da esquerda
    start = start_pos
    l = start
    # ponteiro da direita
    end = end_pos
    r = end

    pivot = arr[start]
    indent = "  " * depth
    
    if verbose:
        print(f"\n{indent}{'─'*50}")
        print(f"{indent}🔄 PARTICIONAMENTO (Nível {depth})")
        print(f"{indent}{'─'*50}")
        print(f"{indent}   Subarray: índices {start} até {end}")
        
        # Mostra o subarray atual
        subarray_visual = []
        for i in range(len(arr)):
            if i == start:
                subarray_visual.append(f"🎯{arr[i]}")  # Pivô
            elif start <= i <= end:
                subarray_visual.append(f"{arr[i]}")
            else:
                subarray_visual.append("·")
        print(f"{indent}   Array: {subarray_visual}")
        print(f"{indent}   🎯 Pivô: {pivot} (índice {start})")
        print(f"{indent}   Left (L): {l}, Right (R): {r}")

    iteration = 0
    while l <= r:
        iteration += 1
        
        if verbose:
            print(f"\n{indent}   --- Iteração {iteration} ---")
            print(f"{indent}   L={l} (valor: {arr[l]}), R={r} (valor: {arr[r]})")
        
        # ponteiro da esquerda vai caminhar em direção ao centro
        while arr[l] < pivot:
            if verbose:
                print(f"{indent}   ➡️  L: arr[{l}]={arr[l]} < pivô({pivot}) → L avança")
            l += 1

        # ponteiro da direita vai caminhar em direção ao centro
        while arr[r] > pivot:
            if verbose:
                print(f"{indent}   ⬅️  R: arr[{r}]={arr[r]} > pivô({pivot}) → R recua")
            r -= 1

        if l <= r:
            # os while estão procurando os valores que não estão na posição correta.
            # quando encontram, trocam de lugar.
            if verbose:
                if l != r:
                    print(f"{indent}   🔀 TROCA: arr[{l}]={arr[l]} ↔ arr[{r}]={arr[r]}")
                else:
                    print(f"{indent}   ⚠️  L e R se encontraram no índice {l}")
            
            (arr[l], arr[r]) = (arr[r], arr[l])
            
            if verbose and l != r:
                # Visualiza o array após a troca
                visual = []
                for i in range(len(arr)):
                    if start <= i <= end:
                        if i == l or i == r:
                            visual.append(f"[{arr[i]}]")
                        else:
                            visual.append(f"{arr[i]}")
                    else:
                        visual.append("·")
                print(f"{indent}   Resultado: {visual}")
            
            l += 1
            r -= 1

    if verbose:
        print(f"\n{indent}   📊 Particionamento concluído!")
        print(f"{indent}   L={l}, R={r}")
        print(f"{indent}   Array atual: {arr}")

    # Chamadas recursivas
    if start < r:
        if verbose:
            print(f"\n{indent}   ⬅️  Processando subarray ESQUERDO: [{start}:{r}]")
        # chama a função recursivamente para a parte esquerda
        quicksort(arr, start, r, verbose, depth + 1)

    if l < end:
        if verbose:
            print(f"\n{indent}   ➡️  Processando subarray DIREITO: [{l}:{end}]")
        # chama a função recursivamente para a parte direita
        quicksort(arr, l, end, verbose, depth + 1)

    # Imprime resultado final apenas na primeira chamada
    if depth == 0 and verbose:
        print(f"\n{'='*60}")
        print(f"✅ ORDENAÇÃO CONCLUÍDA!")
        print(f"{'='*60}")
        print(f"Array final: {arr}")
        print(f"{'='*60}\n")

    return arr


# Exemplo de uso
if __name__ == "__main__":
    print("=" * 60)
    print("DEMONSTRAÇÃO DO QUICK SORT")
    print("=" * 60)
    
    # Teste 1: Array desordenado
    print("\n🔹 TESTE 1: Array desordenado")
    arr1 = [8, 3, 1, 7, 0, 10, 2]
    resultado1 = quicksort(arr1.copy())
    
    # Teste 2: Array pequeno
    print("\n🔹 TESTE 2: Array pequeno")
    arr2 = [5, 2, 8, 1]
    resultado2 = quicksort(arr2.copy())
    
    # Teste 3: Array com elementos repetidos
    print("\n🔹 TESTE 3: Array com elementos repetidos")
    arr3 = [4, 2, 7, 2, 9, 4, 1]
    resultado3 = quicksort(arr3.copy())
