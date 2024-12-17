def bubblesort(arr):
    # Bubble sort algorithm feito manualmente
    #  if arr[0] > arr[1]:
    #      arr[0], arr[1] = arr[1], arr[0]

    #  if arr[1] > arr[2]:
    #      arr[1], arr[2] = arr[2], arr[1]

    #  if arr[2] > arr[3]:
    #      arr[2], arr[3] = arr[3], arr[2]

    #  if arr[3] > arr[4]:
    #      arr[3], arr[4] = arr[4], arr[3]
    print(arr)
    length = len(arr)
    for i in range(length):
        changes = 0
        for j in range(0, length - i - 1):
            print(i, j, arr[j], arr[j + 1], arr)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                changes += 1
        if changes <= 1:
            break
    return arr


# for i in range(len(arr), 0, -1):
#    for j in range(0, i - 1, 1):
#        if arr[j] > arr[j + 1]:
#            arr[j], arr[j + 1] = arr[j + 1], arr[j]
# return arr
