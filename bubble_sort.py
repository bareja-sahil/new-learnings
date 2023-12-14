def sort(nums):
    total = len(nums) - 1
    for i in range(total):
        # run before the last number
        for j in range(total-i):
            if nums[j] > nums[j+1]:
                nums[j+1], nums[j] = nums[j], nums[j+1]
    return nums


data_list = [3, 4, 9, 5, 2, 110, 12, 45]
data_list = [33, 32, 31, 30, 29, 28, 27, 26]
print(data_list)
print(sort(data_list))