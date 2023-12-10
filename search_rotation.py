
def search_rotation(rotated_list, query, low, mid, high):
    if rotated_list[mid] == query:
        return 'found'

        # Check if the left half is sorted
    if rotated_list[low] <= rotated_list[mid]:
        # Check if the target is in the left half
        if rotated_list[low] <= query <= rotated_list[mid]:
            return 'left'
        else:
            return 'right'
    else:  # The right half is sorted
        # Check if the query is in the right half

        if rotated_list[mid] <= query <= rotated_list[high]:
            return 'right'
        else:
            return 'left'


def main(rotated_list, query):
    low = 0
    high = len(rotated_list)-1

    while low <= high:
        print(f"low: {low}")
        print(f"high: {high}")
        mid = (low + high) // 2
        print(f"mid: {mid}")
        result = search_rotation(rotated_list, query, low, mid, high)
        print(result)
        if result == 'found':
            return mid+1
        elif result == 'left':
            high = mid - 1
        elif result == 'right':
            low = mid + 1
    return -1


rotated_list = [19, 25, 29, 31, 3, 5]
# rotated_list = [8, 9, 2, 3, 5, 6, 7]
# rotated_list = [8, 9, 10, 2, 3, 4, 5]
# rotated_list = [5, 55, 6, 6, 9, 9, 9, 9, 9, 10, 11, 12, 3, 3, 3, 3, 4, 4]
# rotated_list = [1, 2, 3, 4, 5, 6]
print(main(rotated_list, 31))