def swap_numbers(arr, po1, po2):
    arr[po2],arr[po1] = arr[po1],arr[po2]
    return arr

arr = [144, 25, 12, 22, 11, 22]

for i in range(len(arr)):
    min_val = i
    for j in range(i + 1, len(arr)):
        if arr[min_val] > arr[j]:
            min_val = j

    arr_swp = swap_numbers(arr, i , min_val)

print ("Sorted array")
print(arr_swp)