def sub_sets(arr, i, res):
        if i == len(arr):
            print(res)
            return
        sub_sets(arr, i+1, res)
        sub_sets(arr, i+1, res+[arr[i]])


sub_sets([1, 2, 3], i=0, res=[])