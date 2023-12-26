import math


class Solution:
    def maxScore(self, nums):
        data_structure = {}
        n = int(len(nums)/2)
        found_list = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                data_structure[(nums[i], nums[j])] = math.gcd(nums[i], nums[j])
        print(data_structure)
        sorted_dict = sorted(data_structure.items(), key= lambda x: x[1], reverse=True)
        j = 0
        max_sum = 0
        print(sorted_dict)
        while n > 0:
            keys, data = sorted_dict[j]
            x, y = keys
            if x in found_list or y in found_list:
                pass
            else:
                found_list.append(x)
                found_list.append(y)
                max_sum = max_sum + data * n
                n -= 1
            j += 1

        return max_sum
print(Solution().maxScore([109497,983516,698308,409009,310455,528595,524079,18036,341150,641864,913962,421869,943382,295019]))