def binary_search(arr, target):
    """
    Implementação de busca binária com prints explicativos.
    
    Args:
        arr: Lista ordenada onde será feita a busca
        target: Elemento que estamos procurando
    
    Returns:
        int: Índice do elemento encontrado ou -1 se não encontrado
    """
    print(f"\n{'='*60}")
    print(f"🔍 INICIANDO BUSCA BINÁRIA")
    print(f"{'='*60}")
    print(f"Array: {arr}")
    print(f"Elemento procurado: {target}")
    print(f"Tamanho do array: {len(arr)}")
    
    left = 0
    right = len(arr) - 1
    iteration = 0
    
    print(f"\n📍 Posição inicial:")
    print(f"   Left (esquerda): {left}")
    print(f"   Right (direita): {right}")
    
    while left <= right:
        iteration += 1
        mid = (left + right) // 2
        
        print(f"\n{'─'*60}")
        print(f"🔄 ITERAÇÃO {iteration}")
        print(f"{'─'*60}")
        print(f"   Left: {left}, Right: {right}")
        print(f"   Mid (meio): {mid}")
        print(f"   Elemento no meio: arr[{mid}] = {arr[mid]}")
        
        # Visualização da área de busca atual
        visual = []
        for i in range(len(arr)):
            if i == mid:
                visual.append(f"[{arr[i]}]")  # Elemento do meio
            elif i >= left and i <= right:
                visual.append(f" {arr[i]} ")   # Área de busca
            else:
                visual.append(f" · ")          # Fora da área de busca
        print(f"   Área de busca: {''.join(visual)}")
        
        # Comparações
        if arr[mid] == target:
            print(f"\n✅ ELEMENTO ENCONTRADO!")
            print(f"   arr[{mid}] = {arr[mid]} == {target}")
            print(f"   Índice: {mid}")
            print(f"   Total de iterações: {iteration}")
            print(f"{'='*60}\n")
            return mid
        
        elif arr[mid] < target:
            print(f"   ⬆️  arr[{mid}] = {arr[mid]} < {target}")
            print(f"   → O elemento está na METADE DIREITA")
            print(f"   → Movendo Left para {mid + 1}")
            left = mid + 1
        
        else:
            print(f"   ⬇️  arr[{mid}] = {arr[mid]} > {target}")
            print(f"   → O elemento está na METADE ESQUERDA")
            print(f"   → Movendo Right para {mid - 1}")
            right = mid - 1
    
    print(f"\n❌ ELEMENTO NÃO ENCONTRADO!")
    print(f"   O elemento {target} não está no array")
    print(f"   Total de iterações: {iteration}")
    print(f"{'='*60}\n")
    return -1


def binary_search_recursive(arr, target, left=None, right=None, iteration=0):
    """
    Implementação recursiva de busca binária com prints explicativos.
    
    Args:
        arr: Lista ordenada onde será feita a busca
        target: Elemento que estamos procurando
        left: Índice esquerdo (início do array)
        right: Índice direito (fim do array)
        iteration: Contador de iterações
    
    Returns:
        int: Índice do elemento encontrado ou -1 se não encontrado
    """
    # Inicialização na primeira chamada
    if left is None and right is None:
        print(f"\n{'='*60}")
        print(f"🔍 INICIANDO BUSCA BINÁRIA RECURSIVA")
        print(f"{'='*60}")
        print(f"Array: {arr}")
        print(f"Elemento procurado: {target}")
        print(f"Tamanho do array: {len(arr)}")
        left = 0
        right = len(arr) - 1
        iteration = 0
        print(f"\n📍 Posição inicial:")
        print(f"   Left (esquerda): {left}")
        print(f"   Right (direita): {right}")
    
    # Caso base: elemento não encontrado
    if left > right:
        print(f"\n❌ ELEMENTO NÃO ENCONTRADO!")
        print(f"   Left ({left}) > Right ({right}) - área de busca esgotada")
        print(f"   O elemento {target} não está no array")
        print(f"   Total de iterações: {iteration}")
        print(f"{'='*60}\n")
        return -1
    
    iteration += 1
    mid = (left + right) // 2
    
    print(f"\n{'─'*60}")
    print(f"🔄 ITERAÇÃO {iteration} (Recursiva)")
    print(f"{'─'*60}")
    print(f"   Left: {left}, Right: {right}")
    print(f"   Mid (meio): {mid}")
    print(f"   Elemento no meio: arr[{mid}] = {arr[mid]}")
    
    # Visualização da área de busca atual
    visual = []
    for i in range(len(arr)):
        if i == mid:
            visual.append(f"[{arr[i]}]")
        elif i >= left and i <= right:
            visual.append(f" {arr[i]} ")
        else:
            visual.append(f" · ")
    print(f"   Área de busca: {''.join(visual)}")
    
    # Elemento encontrado
    if arr[mid] == target:
        print(f"\n✅ ELEMENTO ENCONTRADO!")
        print(f"   arr[{mid}] = {arr[mid]} == {target}")
        print(f"   Índice: {mid}")
        print(f"   Total de iterações: {iteration}")
        print(f"{'='*60}\n")
        return mid
    
    # Buscar na metade direita
    elif arr[mid] < target:
        print(f"   ⬆️  arr[{mid}] = {arr[mid]} < {target}")
        print(f"   → O elemento está na METADE DIREITA")
        print(f"   → Chamada recursiva com Left = {mid + 1}")
        return binary_search_recursive(arr, target, mid + 1, right, iteration)
    
    # Buscar na metade esquerda
    else:
        print(f"   ⬇️  arr[{mid}] = {arr[mid]} > {target}")
        print(f"   → O elemento está na METADE ESQUERDA")
        print(f"   → Chamada recursiva com Right = {mid - 1}")
        return binary_search_recursive(arr, target, left, mid - 1, iteration)


# Exemplo de uso
if __name__ == "__main__":
    # Array ordenado para testes
    array = [2, 5, 8, 12, 16, 23, 38, 45, 56, 67, 78]
    
    print("=" * 60)
    print("DEMONSTRAÇÃO DE BUSCA BINÁRIA")
    print("=" * 60)
    
    # Teste 1: Busca iterativa - elemento existe
    print("\n🔹 TESTE 1: Busca Iterativa (elemento existe)")
    resultado = binary_search(array, 23)
    print(f"Resultado: {resultado}")
    
    # Teste 2: Busca iterativa - elemento não existe
    print("\n🔹 TESTE 2: Busca Iterativa (elemento não existe)")
    resultado = binary_search(array, 50)
    print(f"Resultado: {resultado}")
    
    # Teste 3: Busca recursiva - elemento existe
    print("\n🔹 TESTE 3: Busca Recursiva (elemento existe)")
    resultado = binary_search_recursive(array, 45)
    print(f"Resultado: {resultado}")
    
    # Teste 4: Busca recursiva - elemento não existe
    print("\n🔹 TESTE 4: Busca Recursiva (elemento não existe)")
    resultado = binary_search_recursive(array, 100)
    print(f"Resultado: {resultado}")
