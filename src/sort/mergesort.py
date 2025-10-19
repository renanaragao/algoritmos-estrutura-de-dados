def mergesort(arr, verbose=True, depth=0):
    """
    Implementação do Merge Sort com prints explicativos.
    
    Args:
        arr: Lista a ser ordenada
        verbose: Se True, exibe prints detalhados do processo
        depth: Profundidade da recursão (para indentação)
    
    Returns:
        Lista ordenada
    """
    # Inicialização na primeira chamada
    if depth == 0 and verbose:
        print(f"\n{'='*60}")
        print(f"🔀 MERGE SORT - ORDENAÇÃO POR MESCLAGEM")
        print(f"{'='*60}")
        print(f"Array inicial: {arr}")
        print(f"Tamanho: {len(arr)}")
        print(f"\n💡 Conceito: Divide o array ao meio recursivamente até")
        print(f"   ter arrays de 1 elemento, depois mescla ordenando.")
        print(f"{'='*60}")
    
    indent = "  " * depth
    
    # Caso base: array com 0 ou 1 elemento já está ordenado
    if len(arr) <= 1:
        if verbose:
            print(f"{indent}📌 Caso base: array {arr} já está ordenado")
        return arr
    
    # Divide o array ao meio
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    if verbose:
        print(f"\n{indent}{'─'*50}")
        print(f"{indent}✂️  DIVISÃO (Nível {depth})")
        print(f"{indent}{'─'*50}")
        print(f"{indent}   Array atual: {arr}")
        print(f"{indent}   Meio em índice: {mid}")
        print(f"{indent}   Esquerda: {left_half}")
        print(f"{indent}   Direita: {right_half}")
    
    # Recursivamente ordena as duas metades
    if verbose:
        print(f"\n{indent}⬅️  Processando metade ESQUERDA: {left_half}")
    left_sorted = mergesort(left_half, verbose, depth + 1)
    
    if verbose:
        print(f"\n{indent}➡️  Processando metade DIREITA: {right_half}")
    right_sorted = mergesort(right_half, verbose, depth + 1)
    
    # Mescla as duas metades ordenadas
    if verbose:
        print(f"\n{indent}{'─'*50}")
        print(f"{indent}🔗 MESCLAGEM (Nível {depth})")
        print(f"{indent}{'─'*50}")
        print(f"{indent}   Mesclando:")
        print(f"{indent}   Esquerda: {left_sorted}")
        print(f"{indent}   Direita:  {right_sorted}")
    
    merged = merge(left_sorted, right_sorted, verbose, indent)
    
    if verbose:
        print(f"{indent}   ✅ Resultado da mesclagem: {merged}")
    
    # Imprime resultado final apenas na primeira chamada
    if depth == 0 and verbose:
        print(f"\n{'='*60}")
        print(f"✅ ORDENAÇÃO CONCLUÍDA!")
        print(f"{'='*60}")
        print(f"Array final: {merged}")
        print(f"{'='*60}\n")
    
    return merged


def merge(left, right, verbose=True, indent=""):
    """
    Mescla dois arrays ordenados em um único array ordenado.
    
    Args:
        left: Array esquerdo ordenado
        right: Array direito ordenado
        verbose: Se True, exibe prints detalhados
        indent: String de indentação para prints
    
    Returns:
        Array mesclado e ordenado
    """
    result = []
    i = j = 0
    comparison_count = 0
    
    if verbose:
        print(f"{indent}      Índices iniciais: i=0, j=0")
    
    # Compara elementos de ambos os arrays e adiciona o menor
    while i < len(left) and j < len(right):
        comparison_count += 1
        
        if verbose:
            print(f"{indent}      📍 i={i}, j={j}")
            print(f"{indent}      Comparando: left[{i}]={left[i]} vs right[{j}]={right[j]}")
        
        if left[i] <= right[j]:
            result.append(left[i])
            if verbose:
                print(f"{indent}         ✓ {left[i]} <= {right[j]} → Adiciona {left[i]} de LEFT")
                print(f"{indent}         → i incrementa: {i} → {i + 1}")
            i += 1
        else:
            result.append(right[j])
            if verbose:
                print(f"{indent}         ✓ {left[i]} > {right[j]} → Adiciona {right[j]} de RIGHT")
                print(f"{indent}         → j incrementa: {j} → {j + 1}")
            j += 1
        
        if verbose:
            print(f"{indent}         Resultado parcial: {result}")
            print(f"{indent}         Novos índices: i={i}, j={j}")
    
    # Adiciona os elementos restantes do array esquerdo (se houver)
    if verbose and i < len(left):
        print(f"{indent}      📝 Array RIGHT esgotado (j={j} >= {len(right)})")
        print(f"{indent}      Adicionando elementos restantes de LEFT: {left[i:]}")
    
    while i < len(left):
        result.append(left[i])
        if verbose:
            print(f"{indent}         Adiciona left[{i}]={left[i]}")
        i += 1
    
    # Adiciona os elementos restantes do array direito (se houver)
    if verbose and j < len(right):
        print(f"{indent}      📝 Array LEFT esgotado (i={i} >= {len(left)})")
        print(f"{indent}      Adicionando elementos restantes de RIGHT: {right[j:]}")
    
    while j < len(right):
        result.append(right[j])
        if verbose:
            print(f"{indent}         Adiciona right[{j}]={right[j]}")
        j += 1
    
    if verbose:
        print(f"{indent}      Total de comparações: {comparison_count}")
    
    return result


# Exemplo de uso
if __name__ == "__main__":
    print("=" * 60)
    print("DEMONSTRAÇÃO DO MERGE SORT")
    print("=" * 60)
    
    # Teste 1: Array desordenado
    print("\n🔹 TESTE 1: Array desordenado")
    arr1 = [38, 27, 43, 3, 9, 82, 10]
    resultado1 = mergesort(arr1.copy())
    
    # Teste 2: Array pequeno
    print("\n🔹 TESTE 2: Array pequeno")
    arr2 = [5, 2, 8, 1]
    resultado2 = mergesort(arr2.copy())
    
    # Teste 3: Array já ordenado
    print("\n🔹 TESTE 3: Array já ordenado")
    arr3 = [1, 2, 3, 4, 5]
    resultado3 = mergesort(arr3.copy())
    
    # Teste 4: Array muito pequeno
    print("\n🔹 TESTE 4: Array de 3 elementos")
    arr4 = [8, 5, 10]
    resultado4 = mergesort(arr4.copy())
