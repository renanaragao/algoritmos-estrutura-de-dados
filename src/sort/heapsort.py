class BinaryHeap:
    _data = []

    def insert(self, value):
        self._data.append(value)

        if len(self._data) == 1:
            return None

        i = len(self._data) - 1
        p = BinaryHeap.parent(i)

        # O while é executado enquanto o valor do nó atual for maior que o valor do nó pai.
        # O isBigger é para manter o Binary Heap como um Max Heap.
        while BinaryHeap.isBigger(self._data[i], self._data[p]):
            BinaryHeap.swap(self._data, i, p)

            i = p
            p = BinaryHeap.parent(i)

            if p == -1:
                break

    def dequeue(self):
        if len(self._data) == 0:
            return None

        result = self._data[0]

        self._data.pop(len(self._data) - 1)
        self._data[0] = self._data[len(self._data) - 1]

        BinaryHeap._heapfy(self._data, len(self._data), 0)

        return result

    @staticmethod
    def heapSort(data):
        BinaryHeap.heapfy(data, len(data))

        for i in range(len(data) - 1, -1, -1):
            BinaryHeap.swap(data, 0, i)

            BinaryHeap._heapfy(data, (i - 1), 0)

        return data

    @staticmethod
    def parent(nodeIndex):
        if nodeIndex == 0:
            return -1

        return (nodeIndex - 1) // 2

    @staticmethod
    def isBigger(valorA, valorB):
        return valorA > valorB

    @staticmethod
    def heapfy(data, size):
        if size <= 1:
            return None

        # O size / 2 - 1 é para pegar o último nó que tem filhos.
        for i in range(size // 2 - 1, -1, -1):
            BinaryHeap._heapfy(data, size, i)

    @staticmethod
    def _heapfy(data, size, index):
        biggest = index
        left = BinaryHeap.left(data, index)
        right = BinaryHeap.right(data, index)

        if left < size and BinaryHeap.isBigger(data[left], data[biggest]):
            biggest = left

        if right < size and BinaryHeap.isBigger(data[right], data[biggest]):
            biggest = right

        if biggest == -1:
            return None

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
        data[indexA], data[indexB] = data[indexB], data[indexA]

        return data

    @staticmethod
    def returnResult(result, data):
        if result < len(data):
            return result

        return -1