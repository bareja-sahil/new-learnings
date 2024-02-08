def search_2d(matrix, target):

    def bin_search(row, n, target):
        start = 0
        end = n-1
        while start <= end:
            mid = (start + end) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return False

    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        if matrix[i][0] <= target <= matrix[i][n-1]:
            return bin_search(i, n, target)
    return False

print(search_2d(matrix =[[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))
print(search_2d(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13))