def sort(nums):
    total = len(nums)
    for i in range(1, total):
        j = i-1
        while j >= 0 and nums[j] > nums[j+1]:
            # print(j)
            # print(f"nums[j] {nums[j]}")
            # print(f"nums[j+1] {nums[j+1]}")
            nums[j], nums[j+1] = nums[j+1], nums[j]
            # print(f"nums {nums}")
            j -= 1
        print(nums)
    return nums

data_list = [3, 4, 9, 5, 2, 110, 12, 45]
# data_list = [6, 9, 2, 3]
# data_list = [33, 32, 31, 30, 29, 28, 27, 26]
print(data_list)
print(sort(data_list))