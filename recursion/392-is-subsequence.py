def sub_sequences(arr):
    n = len(arr)
    super_set = pow(2, n)
    for i in range(super_set):
        x = []
        for j in range(n):
            if i & (1 << j) != 0:
                x.append(arr[j])
        print(x)


sub_sequences('abc')

