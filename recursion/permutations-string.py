def permutation_string(nums):
    results = []
    def recurse(nums, index):
        nonlocal results
        if index >= len(nums):
            results.append(nums.copy())
            return
        j = index
        while j < len(nums):
            nums[index], nums[j] = nums[j], nums[index]
            recurse(nums, index + 1)
            nums[index], nums[j] = nums[j], nums[index]
            j += 1

    recurse(nums, 0)
    return results

str1 = [1, 2, 3]
print(permutation_string(str1))