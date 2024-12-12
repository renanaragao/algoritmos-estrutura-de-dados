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
    length = len(arr)
    for i in range(length):
        for j in range(0, length-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr
