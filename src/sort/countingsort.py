def countingsort(arr, verbose=True):
    """
    Implementação do Counting Sort com prints explicativos.
    
    Args:
        arr: Lista a ser ordenada (deve conter apenas números inteiros não negativos)
        verbose: Se True, exibe prints detalhados do processo
    
    Returns:
        Lista ordenada
    """
    if verbose:
        print(f"\n{'='*60}")
        print(f"🔢 COUNTING SORT - ORDENAÇÃO POR CONTAGEM")
        print(f"{'='*60}")
        print(f"Array inicial: {arr}")
        print(f"Tamanho: {len(arr)}")
        print(f"\n💡 Conceito: Conta a frequência de cada valor e reconstrói")
        print(f"   o array ordenado baseado nessas contagens.")
        print(f"⚠️  Funciona apenas com inteiros não negativos!")
        print(f"{'='*60}")
    
    # Verifica se o array está vazio
    if len(arr) == 0:
        if verbose:
            print(f"\n❌ Array vazio! Retornando array vazio.")
        return arr
    
    # Verifica se há números negativos ou não inteiros
    if verbose:
        print(f"\n🔍 Verificando valores do array...")
    
    for i, val in enumerate(arr):
        if not isinstance(val, int) or val < 0:
            if verbose:
                print(f"\n❌ ERRO: arr[{i}]={val} não é um inteiro não negativo!")
                print(f"   Counting Sort requer apenas inteiros >= 0")
                print(f"{'='*60}\n")
            raise ValueError(f"Counting Sort requer apenas inteiros não negativos. Encontrado: {val}")
    
    if verbose:
        print(f"   ✓ Todos os valores são inteiros não negativos")
    
    # Encontra o valor máximo para determinar o tamanho do array de contagem
    max_val = max(arr)
    min_val = min(arr)
    
    if verbose:
        print(f"\n{'─'*60}")
        print(f"📊 FASE 1: Análise do Range")
        print(f"{'─'*60}")
        print(f"   Valor mínimo: {min_val}")
        print(f"   Valor máximo: {max_val}")
        print(f"   Range: {max_val - min_val + 1}")
    
    # Cria o array de contagem
    range_size = max_val - min_val + 1
    count = [0] * range_size
    
    if verbose:
        print(f"\n{'─'*60}")
        print(f"📈 FASE 2: Contagem de Frequências")
        print(f"{'─'*60}")
        print(f"   Array de contagem inicial: {count}")
        print(f"   Índices representam valores de {min_val} até {max_val}")
    
    # Conta a ocorrência de cada elemento
    for i, num in enumerate(arr):
        index = num - min_val
        
        if verbose:
            print(f"\n   Iteração {i + 1}/{len(arr)} - Processando arr[{i}]={num}:")
            print(f"      → Índice no count: {index} (valor {num} - min {min_val})")
            print(f"      → count[{index}] antes: {count[index]}")
        
        count[index] += 1
        
        if verbose:
            print(f"      → count[{index}] depois: {count[index]}")
            
            # Visualização do array de contagem com destaque
            visual = []
            for j, c in enumerate(count):
                if j == index:
                    visual.append(f"[{c}]")
                else:
                    visual.append(f" {c} ")
            print(f"      → Array count: {' '.join(visual)}")
            print(f"      📊 Status count: {count}")
    
    if verbose:
        print(f"\n   ✅ Contagem completa!")
        print(f"   Array de contagem final: {count}")
        
        # Mostra frequência de cada número
        print(f"\n   📊 Frequência dos valores:")
        for i, c in enumerate(count):
            if c > 0:
                valor = i + min_val
                print(f"      Valor {valor}: aparece {c} vez(es)")
    
    # Modifica o array de contagem para conter posições acumuladas
    if verbose:
        print(f"\n{'─'*60}")
        print(f"🔄 FASE 3: Contagem Acumulada (Posições)")
        print(f"{'─'*60}")
        print(f"   📊 Status count inicial: {count}")
    
    for i in range(1, len(count)):
        if verbose:
            print(f"\n   Iteração {i}/{len(count)-1}:")
            print(f"      count[{i}] = count[{i}] + count[{i-1}]")
            print(f"      count[{i}] = {count[i]} + {count[i-1]}", end="")
        
        count[i] += count[i - 1]
        
        if verbose:
            print(f" = {count[i]}")
            print(f"      📊 Status count: {count}")
    
    if verbose:
        print(f"\n   ✅ Array de posições final: {count}")
        print(f"   Cada valor indica: quantos elementos são <= ao valor correspondente")
    
    # Constrói o array de saída
    output = [0] * len(arr)
    
    if verbose:
        print(f"\n{'─'*60}")
        print(f"🏗️  FASE 4: Construção do Array Ordenado")
        print(f"{'─'*60}")
        print(f"   Array output inicial: {output}")
        print(f"   Processando de trás para frente para manter estabilidade")
    
    # Percorre o array original de trás para frente (para manter estabilidade)
    iteration = 1
    for i in range(len(arr) - 1, -1, -1):
        num = arr[i]
        index = num - min_val
        position = count[index] - 1
        output[position] = num
        
        if verbose:
            print(f"\n   Iteração {iteration}/{len(arr)} - Processando arr[{i}]={num}:")
            print(f"      → Índice no count: {index}")
            print(f"      → Posição no output: {position} (count[{index}]-1)")
            print(f"      → output[{position}] = {num}")
            print(f"      → count[{index}] antes: {count[index]}")
        
        count[index] -= 1
        
        if verbose:
            print(f"      → count[{index}] depois: {count[index]}")
            print(f"      📊 Status count: {count}")
            
            # Visualização do output
            visual = []
            for j, val in enumerate(output):
                if j == position:
                    visual.append(f"[{val}]")
                elif val == 0 and j < len(arr):
                    visual.append(" · ")
                else:
                    visual.append(f" {val} ")
            print(f"      → Output: {' '.join(visual)}")
        
        iteration += 1
    
    if verbose:
        print(f"\n{'='*60}")
        print(f"✅ ORDENAÇÃO CONCLUÍDA!")
        print(f"{'='*60}")
        print(f"Array original: {arr}")
        print(f"Array ordenado: {output}")
        print(f"\n📊 COMPLEXIDADE:")
        print(f"   Tempo: O(n + k) onde n={len(arr)}, k={range_size}")
        print(f"   Espaço: O(n + k)")
        print(f"   Estável: SIM")
        print(f"{'='*60}\n")
    
    return output


# Exemplo de uso
if __name__ == "__main__":
    print("=" * 60)
    print("DEMONSTRAÇÃO DO COUNTING SORT")
    print("=" * 60)
    
    # Teste 1: Array com números pequenos
    print("\n🔹 TESTE 1: Array com números pequenos")
    arr1 = [4, 2, 2, 8, 3, 3, 1]
    resultado1 = countingsort(arr1.copy())
    
    # Teste 2: Array já ordenado
    print("\n🔹 TESTE 2: Array já ordenado")
    arr2 = [1, 2, 3, 4, 5]
    resultado2 = countingsort(arr2.copy())
    
    # Teste 3: Array com valores repetidos
    print("\n🔹 TESTE 3: Array com muitos valores repetidos")
    arr3 = [5, 5, 5, 2, 2, 8]
    resultado3 = countingsort(arr3.copy())
    
    # Teste 4: Array com range maior
    print("\n🔹 TESTE 4: Array com range de 0 a 10")
    arr4 = [10, 0, 5, 2, 8, 3]
    resultado4 = countingsort(arr4.copy())
    
    # Teste 5: Tentativa com número negativo (deve falhar)
    print("\n🔹 TESTE 5: Tentativa com número negativo (deve gerar erro)")
    try:
        arr5 = [5, -2, 8, 1]
        resultado5 = countingsort(arr5.copy())
    except ValueError as e:
        print(f"\n✓ Erro capturado corretamente!")
