
def test_rotation(rotated_list, low, mid, high):
    if mid > 0 and (rotated_list[mid-1] > rotated_list[mid]):
        return 'found'
    if (mid < len(rotated_list) - 1) and (rotated_list[mid+1] < rotated_list[mid]):
        return 'found+1'
    elif rotated_list[low] > rotated_list[mid]:
        return 'left'
    else:
        return 'right'


def main(rotated_list):
    low = 0
    high = len(rotated_list)-1

    while low <= high:
        print(f"low: {low}")
        print(f"high: {high}")
        mid = (low + high) // 2
        result = test_rotation(rotated_list, low, mid, high)
        print(result)
        if result == 'found':
            return mid
        elif result == 'found+1':
            return mid + 1
        elif result == 'left':
            high = mid - 1
        elif result == 'right':
            low = mid + 1
    return -1


# rotated_list = [19, 25, 29, 3, 5, 6]
# rotated_list = [8, 9, 2, 3, 5, 6, 7]
# rotated_list = [8, 9, 10, 2, 3, 4, 5]
# rotated_list = [5, 5, 6, 6, 9, 9, 9, 9, 9, 10, 11, 12, 3, 3, 3, 3, 4, 4]
# rotated_list = [1, 2, 3, 4, 5, 6]
rotated_list = [5, 6, 9, 2, 3, 4, 5]
print(main(rotated_list))