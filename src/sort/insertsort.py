def insertionsort(arr, verbose=True):
    """
    Implementação do Insertion Sort com prints explicativos.
    
    Args:
        arr: Lista a ser ordenada
        verbose: Se True, exibe prints detalhados do processo
    
    Returns:
        Lista ordenada
    """
    if verbose:
        print(f"\n{'='*60}")
        print(f"🎯 INSERTION SORT - ORDENAÇÃO POR INSERÇÃO")
        print(f"{'='*60}")
        print(f"Array inicial: {arr}")
        print(f"Tamanho: {len(arr)}")
        print(f"\n💡 Conceito: Constrói o array ordenado um elemento por vez,")
        print(f"   inserindo cada elemento na posição correta da parte ordenada.")
        print(f"\n🎴 Analogia: Como ordenar cartas de baralho na mão!")
        print(f"{'='*60}")
    
    # Verifica se o array está vazio ou tem apenas um elemento
    if len(arr) <= 1:
        if verbose:
            print(f"\n✅ Array já está ordenado (tamanho {len(arr)})")
            print(f"{'='*60}\n")
        return arr
    
    comparisons = 0
    shifts = 0
    
    # Começa do segundo elemento (índice 1)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        if verbose:
            print(f"\n{'─'*60}")
            print(f"🔄 ITERAÇÃO {i} - Inserindo elemento arr[{i}]={key}")
            print(f"{'─'*60}")
            
            # Visualiza a parte ordenada e não ordenada
            visual = []
            for k in range(len(arr)):
                if k < i:
                    visual.append(f"✓{arr[k]}")
                elif k == i:
                    visual.append(f"[{arr[k]}]")
                else:
                    visual.append(f"·{arr[k]}")
            print(f"   Estado: {' '.join(visual)}")
            print(f"   Legenda: ✓=ordenada | [X]=key | ·X=não ordenada")
            print(f"\n   🔑 Key = {key} (elemento a ser inserido)")
            print(f"   📍 Comparando com a parte ordenada (índices 0 até {i-1})")
        
        # Move elementos maiores que key uma posição à frente
        iteration = 0
        if verbose:
            print(f"\n   ⬅️  Deslocando elementos maiores que {key}:")
            print(f"   📍 Valor inicial de j: {j}")
        
        while j >= 0 and arr[j] > key:
            comparisons += 1
            shifts += 1
            iteration += 1
            
            if verbose:
                print(f"\n      Passo {iteration}:")
                print(f"         📍 j atual = {j}")
                print(f"         Comparando: arr[{j}]={arr[j]} > key={key}? ✅ SIM")
                print(f"         → arr[{j+1}] = arr[{j}] (desloca {arr[j]} para direita)")
            
            arr[j + 1] = arr[j]
            
            if verbose:
                # Visualiza o array durante o deslocamento
                visual = []
                for k in range(len(arr)):
                    if k == j + 1:
                        visual.append(f"[{arr[k]}]")
                    elif k <= i:
                        visual.append(f" {arr[k]} ")
                    else:
                        visual.append(f"·{arr[k]}")
                print(f"         Array: {' '.join(visual)}")
            # Vai decrementando para quando chegar a -1 sair do loop
            j -= 1
            
            if verbose:
                print(f"         → j decrementa: {j + 1} → {j}")
        
        # Última comparação (se houver)
        if j >= 0:
            comparisons += 1
            if verbose:
                print(f"\n      Passo {iteration + 1}:")
                print(f"         📍 j atual = {j}")
                print(f"         Comparando: arr[{j}]={arr[j]} > key={key}? ❌ NÃO")
                print(f"         ✋ Para de deslocar!")
        else:
            if verbose and iteration > 0:
                print(f"\n      📍 j chegou a {j} (antes do início do array)")
                print(f"         ✋ Para de deslocar!")
        
        # Insere o key na posição correta
        arr[j + 1] = key
        
        if verbose:
            print(f"\n   ✅ Inserindo key={key} na posição {j+1}")
            print(f"   📍 Valor final de j: {j}")
            
            # Visualiza o array após a inserção
            visual = []
            for k in range(len(arr)):
                if k == j + 1:
                    visual.append(f"[{arr[k]}]")
                elif k <= i:
                    visual.append(f"✓{arr[k]}")
                else:
                    visual.append(f"·{arr[k]}")
            print(f"   Array: {' '.join(visual)}")
            
            # Mostra o array completo ordenado até agora
            print(f"\n   📊 Array após iteração {i}: {arr[:i+1]} | {arr[i+1:]}")
            print(f"      Ordenada: {arr[:i+1]} ✓")
            print(f"      Não ordenada: {arr[i+1:]}")
    
    if verbose:
        print(f"\n{'='*60}")
        print(f"✅ ORDENAÇÃO CONCLUÍDA!")
        print(f"{'='*60}")
        print(f"Array final ordenado: {arr}")
        print(f"\n📊 ESTATÍSTICAS:")
        print(f"   Total de comparações: {comparisons}")
        print(f"   Total de deslocamentos: {shifts}")
        print(f"\n📊 COMPLEXIDADE:")
        print(f"   Melhor caso: O(n) - array já ordenado")
        print(f"   Caso médio: O(n²)")
        print(f"   Pior caso: O(n²) - array em ordem decrescente")
        print(f"   Espaço: O(1) - in-place")
        print(f"   Estável: SIM")
        print(f"\n💡 QUANDO USAR:")
        print(f"   ✅ Arrays pequenos (< 50 elementos)")
        print(f"   ✅ Arrays quase ordenados")
        print(f"   ✅ Inserção online (elementos chegam um a um)")
        print(f"{'='*60}\n")
    
    return arr


# Exemplo de uso
if __name__ == "__main__":
    print("=" * 60)
    print("DEMONSTRAÇÃO DO INSERTION SORT")
    print("=" * 60)
    
    # Teste 1: Array pequeno não ordenado
    print("\n🔹 TESTE 1: Array pequeno")
    arr1 = [5, 2, 4, 6, 1, 3]
    resultado1 = insertionsort(arr1.copy())
    
    # Teste 2: Array já ordenado (melhor caso)
    print("\n🔹 TESTE 2: Array já ordenado (melhor caso)")
    arr2 = [1, 2, 3, 4, 5]
    resultado2 = insertionsort(arr2.copy())
    
    # Teste 3: Array em ordem decrescente (pior caso)
    print("\n🔹 TESTE 3: Array em ordem decrescente (pior caso)")
    arr3 = [5, 4, 3, 2, 1]
    resultado3 = insertionsort(arr3.copy())
    
    # Teste 4: Array com elementos duplicados
    print("\n🔹 TESTE 4: Array com duplicados")
    arr4 = [3, 1, 4, 1, 5, 9, 2, 6]
    resultado4 = insertionsort(arr4.copy())
    
    # Teste 5: Array muito pequeno
    print("\n🔹 TESTE 5: Arrays de tamanho especial")
    print("\nArray vazio:")
    arr5 = []
    resultado5 = insertionsort(arr5.copy())
    
    print("\nArray com 1 elemento:")
    arr6 = [42]
    resultado6 = insertionsort(arr6.copy())
    
    print("\nArray com 2 elementos:")
    arr7 = [2, 1]
    resultado7 = insertionsort(arr7.copy())
