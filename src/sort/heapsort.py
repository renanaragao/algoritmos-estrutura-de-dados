class BinaryHeap:
    def __init__(self, verbose=True):
        """
        Inicializa um Binary Heap (Max Heap).
        
        Args:
            verbose: Se True, exibe prints detalhados do processo
        """
        self._data = []
        self.verbose = verbose
        
        if verbose:
            print(f"\n{'='*60}")
            print(f"🌳 BINARY HEAP (MAX HEAP) - Estrutura de Dados")
            print(f"{'='*60}")
            print(f"💡 Conceito: Árvore binária onde cada pai é maior que")
            print(f"   seus filhos. Raiz sempre tem o maior valor.")
            print(f"{'='*60}\n")

    def insert(self, value):
        """Insere um valor no heap e mantém a propriedade do max heap."""
        self._data.append(value)

        if self.verbose:
            print(f"➕ Inserindo: {value}")
            print(f"   Heap antes: {self._data[:-1] if len(self._data) > 1 else []}")
            print(f"   Posição inicial: índice {len(self._data) - 1}")

        if len(self._data) == 1:
            if self.verbose:
                print(f"   ✅ Primeiro elemento! Heap: {self._data}\n")
            return None

        i = len(self._data) - 1
        p = BinaryHeap.parent(i)

        if self.verbose:
            print(f"   🔄 Bubble Up (subir o valor se necessário)")

        iterations = 0
        # O while é executado enquanto o valor do nó atual for maior que o valor do nó pai.
        while BinaryHeap.isBigger(self._data[i], self._data[p]):
            iterations += 1
            if self.verbose:
                print(f"   Iteração {iterations}: arr[{i}]={self._data[i]} > arr[{p}]={self._data[p]}")
                print(f"      🔀 Trocando: {self._data[i]} ↔ {self._data[p]}")
            
            BinaryHeap.swap(self._data, i, p)

            i = p
            p = BinaryHeap.parent(i)

            if p == -1:
                if self.verbose:
                    print(f"      🎯 Chegou à raiz!")
                break

        if self.verbose:
            print(f"   ✅ Heap após inserção: {self._data}")
            self._print_tree()
            print()

    def dequeue(self):
        """Remove e retorna o maior elemento (raiz) do heap."""
        if len(self._data) == 0:
            if self.verbose:
                print(f"❌ Heap vazio! Não há elementos para remover.\n")
            return None

        result = self._data[0]
        
        if self.verbose:
            print(f"🔽 Removendo raiz (maior elemento): {result}")
            print(f"   Heap antes: {self._data}")

        # Move o último elemento para a raiz
        self._data[0] = self._data[len(self._data) - 1]
        self._data.pop()

        if self.verbose and len(self._data) > 0:
            print(f"   Moveu último elemento para raiz: {self._data[0]}")
            print(f"   🔄 Heapify down (descer o valor se necessário)")

        if len(self._data) > 0:
            BinaryHeap._heapfy(self._data, len(self._data), 0, self.verbose)

        if self.verbose:
            print(f"   ✅ Heap após remoção: {self._data}")
            if len(self._data) > 0:
                self._print_tree()
            print()

        return result

    def _print_tree(self):
        """Imprime uma representação visual simplificada da árvore."""
        if len(self._data) == 0:
            return
        
        print(f"   Visualização da árvore:")
        levels = []
        level = 0
        while 2**level - 1 < len(self._data):
            start = 2**level - 1
            end = min(2**(level+1) - 1, len(self._data))
            levels.append(self._data[start:end])
            level += 1
        
        for i, level in enumerate(levels):
            indent = "      " + "  " * (len(levels) - i - 1)
            print(f"{indent}{level}")

    @staticmethod
    def heapSort(data, verbose=True):
        """
        Ordena um array usando Heap Sort.
        
        Args:
            data: Lista a ser ordenada
            verbose: Se True, exibe prints detalhados do processo
        
        Returns:
            Lista ordenada
        """
        if verbose:
            print(f"\n{'='*60}")
            print(f"📊 HEAP SORT - ORDENAÇÃO POR HEAP")
            print(f"{'='*60}")
            print(f"Array inicial: {data}")
            print(f"Tamanho: {len(data)}")
            print(f"\n💡 Conceito: Constrói um max heap e remove repetidamente")
            print(f"   o maior elemento, colocando-o no final do array.")
            print(f"{'='*60}")

        # Fase 1: Construir o Max Heap
        if verbose:
            print(f"\n{'─'*60}")
            print(f"FASE 1: Construindo Max Heap")
            print(f"{'─'*60}")
        
        BinaryHeap.heapfy(data, len(data), verbose)
        
        if verbose:
            print(f"✅ Max Heap construído: {data}")

        # Fase 2: Extrair elementos um por um
        if verbose:
            print(f"\n{'─'*60}")
            print(f"FASE 2: Extraindo elementos e ordenando")
            print(f"{'─'*60}")

        for i in range(len(data) - 1, 0, -1):
            if verbose:
                print(f"\n🔄 Passo {len(data) - i}/{len(data) - 1}")
                print(f"   Trocando raiz (máximo) com último elemento não ordenado")
                print(f"   arr[0]={data[0]} ↔ arr[{i}]={data[i]}")
            
            BinaryHeap.swap(data, 0, i)
            
            if verbose:
                # Visualização
                visual = []
                for j in range(len(data)):
                    if j < i:
                        visual.append(f"{data[j]}")
                    elif j == i:
                        visual.append(f"✓{data[j]}")
                    else:
                        visual.append(f"✓{data[j]}")
                print(f"   Array: {visual}")
                print(f"   🔄 Restaurando propriedade do heap (índices 0 até {i-1})")

            BinaryHeap._heapfy(data, i, 0, verbose, indent="      ")

        if verbose:
            print(f"\n{'='*60}")
            print(f"✅ ORDENAÇÃO CONCLUÍDA!")
            print(f"{'='*60}")
            print(f"Array final: {data}")
            print(f"{'='*60}\n")

        return data

    @staticmethod
    def parent(nodeIndex):
        """Retorna o índice do nó pai."""
        if nodeIndex == 0:
            return -1
        return (nodeIndex - 1) // 2

    @staticmethod
    def isBigger(valorA, valorB):
        """Verifica se valorA é maior que valorB."""
        return valorA > valorB

    @staticmethod
    def heapfy(data, size, verbose=False):
        """Constrói um max heap a partir de um array desordenado."""
        if size <= 1:
            return None

        # O size / 2 - 1 é para pegar o último nó que tem filhos.
        if verbose:
            print(f"   Processando nós com filhos (de {size // 2 - 1} até 0)")
        
        for i in range(size // 2 - 1, -1, -1):
            if verbose:
                print(f"   Heapify no índice {i} (valor: {data[i]})")
            BinaryHeap._heapfy(data, size, i, verbose, indent="      ")

    @staticmethod
    def _heapfy(data, size, index, verbose=False, indent="   "):
        """
        Mantém a propriedade do max heap a partir de um índice.
        Assume que as subárvores esquerda e direita já são heaps válidos.
        """
        biggest = index
        left = BinaryHeap.left(data, index)
        right = BinaryHeap.right(data, index)

        if verbose:
            print(f"{indent}Analisando índice {index} (valor: {data[index]})")
            left_val = data[left] if left < size and left != -1 else None
            right_val = data[right] if right < size and right != -1 else None
            print(f"{indent}   Filhos: esq[{left}]={left_val}, dir[{right}]={right_val}")

        if left < size and BinaryHeap.isBigger(data[left], data[biggest]):
            biggest = left
            if verbose:
                print(f"{indent}   Filho esquerdo {data[left]} > pai {data[index]}")

        if right < size and BinaryHeap.isBigger(data[right], data[biggest]):
            biggest = right
            if verbose:
                print(f"{indent}   Filho direito {data[right]} > maior atual {data[biggest]}")

        if biggest == -1:
            return None

        if biggest != index:
            if verbose:
                print(f"{indent}   🔀 Troca necessária: arr[{index}]={data[index]} ↔ arr[{biggest}]={data[biggest]}")
            
            BinaryHeap.swap(data, index, biggest)
            
            if verbose:
                print(f"{indent}   Continuando heapify recursivamente no índice {biggest}")
            
            BinaryHeap._heapfy(data, size, biggest, verbose, indent)
        else:
            if verbose:
                print(f"{indent}   ✓ Propriedade do heap mantida")

    @staticmethod
    def left(data, nodeIndex):
        """Retorna o índice do filho esquerdo."""
        result = (2 * nodeIndex) + 1
        return BinaryHeap.returnResult(result, data)

    @staticmethod
    def right(data, nodeIndex):
        """Retorna o índice do filho direito."""
        result = (2 * nodeIndex) + 2
        return BinaryHeap.returnResult(result, data)

    @staticmethod
    def swap(data, indexA, indexB):
        """Troca dois elementos no array."""
        data[indexA], data[indexB] = data[indexB], data[indexA]
        return data

    @staticmethod
    def returnResult(result, data):
        """Verifica se o índice está dentro dos limites do array."""
        if result < len(data):
            return result
        return -1


# Exemplo de uso
if __name__ == "__main__":
    print("=" * 60)
    print("DEMONSTRAÇÃO DO HEAP SORT E BINARY HEAP")
    print("=" * 60)
    
    # Teste 1: Binary Heap com inserções
    print("\n🔹 TESTE 1: Construindo Binary Heap com inserções")
    heap = BinaryHeap(verbose=True)
    values = [4, 2, 8, 7, 1, 5]
    
    for value in values:
        heap.insert(value)
    
    print("Removendo elementos do heap (em ordem decrescente):")
    while len(heap._data) > 0:
        removed = heap.dequeue()
        print(f"Removido: {removed}")
    
    # Teste 2: Heap Sort
    print("\n" + "="*60)
    print("\n🔹 TESTE 2: Heap Sort em array desordenado")
    arr = [4, 10, 3, 5, 1, 8, 2, 7]
    resultado = BinaryHeap.heapSort(arr.copy(), verbose=True)
    
    # Teste 3: Heap Sort em array pequeno
    print("\n🔹 TESTE 3: Heap Sort em array pequeno")
    arr2 = [9, 3, 7, 1]
    resultado2 = BinaryHeap.heapSort(arr2.copy(), verbose=True)