def max_product(arr):
    i, j = 0, 0

    while i <= len(arr) - 1:
        prev_i_num = arr[i]
        print("J's value: ", j)
        # print(prev_i_num)
        if j > len(arr) - 1:
            print("ran1")
            j = 0
        if arr[j] == arr[i]:
            print("ran2")
            j += 1
        if arr[j] < arr[i]:
            print("ran3")
            arr[i] = arr[j]
            arr[j] = prev_i_num
            j += 1
        if arr[j] > arr[i]:
            print("ran4")
            j += 1


arr = [1, 7, 3, 4, 9, 5]
max_product(arr)

# print(1 < 1)
