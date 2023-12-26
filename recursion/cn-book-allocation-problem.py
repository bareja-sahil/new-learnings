def book_allocation(arr):
    end = sum(arr)
    start = 1
    min_list = []

    def is_possible(arr, mid):
        total_students = 2
        book_sum = 0
        students = 1
        for idx, data in enumerate(arr):
            if book_sum + arr[idx] <= mid:
                book_sum += arr[idx]
            else:
                students += 1
                book_sum = arr[idx]
                if students > total_students:
                    return False
        return True

    def binary_search(start, end, arr):
        nonlocal min_list
        mid = (start + end) // 2
        if start > end:
            return
        if is_possible(arr, mid):
            min_list.append(mid)
            binary_search(start, mid - 1, arr)
        else:
            binary_search(mid+1, end, arr)
    binary_search(start, end, arr)
    print(min_list)

book_allocation([10, 20, 30, 40])

