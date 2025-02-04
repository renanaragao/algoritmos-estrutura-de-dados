def quicksort(arr, start_pos=None, end_pos=None):
    # ponteiro da esquerda
    start = start_pos if start_pos is not None else 0
    l = start
    # ponteiro da direita
    end = end_pos if end_pos is not None else len(arr) - 1
    r = end

    pivot = arr[start]

    while l <= r:
        # ponteiro da esquerda vai caminhar em diração ao centro
        while arr[l] < pivot:
            l += 1

        # ponteiro da direita vai caminhar em direção ao centro
        while arr[r] > pivot:
            r -= 1

        if l <= r:
            # os while estão procurando os valores que não estão na posição correta.
            # quando encontram, trocam de lugar.
            (arr[l], arr[r]) = (arr[r], arr[l])
            l += 1
            r -= 1

    if start < r:
        # chama a função recursivamente para a parte esquerda
        quicksort(arr, start, r)

    if l < end:
        # chama a função recursivamente para a parte direita
        quicksort(arr, l, end)

    return arr
