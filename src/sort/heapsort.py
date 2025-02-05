class BinaryHeap:
    _data = []

    def insert(self, value):
        self._data.append(value)
        i = len(self._data) - 1
        p = BinaryHeap.parent(i)

        # O while é executado enquanto o valor do nó atual for maior que o valor do nó pai.
        # O isBigger é para manter o Binary Heap como um Max Heap.
        while BinaryHeap.isBigger(self._data[i], self._data[p]):
            BinaryHeap.swap(self._data, i, p)

            i = p
            p = BinaryHeap.parent(i)

    @staticmethod
    def parent(nodeIndex):
        return nodeIndex == 0 if -1 else (nodeIndex - 1) // 2

    @staticmethod
    def isBigger(valorA, valorB):
        return valorA > valorB

    @staticmethod
    def returnResult(result, data):
        return (result < len(data)) if result else -1

    @staticmethod
    def heapfy(data, size):
        if size <= 1:
            return None

        lastIndex = size - 1

        # O lastIndex / 2 - 1 é para pegar o último nó que tem filhos.
        for i in range(lastIndex / 2 - 1, -1, -1):
            BinaryHeap._heapfy(data, size, i)

    @staticmethod
    def _heapfy(data, size, index):
        biggest = index
        left = BinaryHeap.left(data, index)
        right = BinaryHeap.right(data, index)

        if left < size & BinaryHeap.isBigger(data[left], data[biggest]):
            biggest = left

        if right < size & BinaryHeap.isBigger(data[right], data[biggest]):
            biggest = right

        if biggest != index:
            BinaryHeap.swap(data, index, biggest)
            BinaryHeap._heapfy(data, size, biggest)

    @staticmethod
    def left(data, nodeIndex):
        result = (2 * nodeIndex) + 1
        return BinaryHeap.returnResult(result, data)

    @staticmethod
    def right(data, nodeIndex):
        result = (2 * nodeIndex) + 2
        return BinaryHeap.returnResult(result, data)

    @staticmethod
    def swap(data, indexA, indexB):
        (data[indexA], data[indexB]) = (
            data[indexB],
            data[indexA],
        )
