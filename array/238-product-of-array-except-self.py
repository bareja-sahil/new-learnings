class Solution:
    def productExceptSelf(self, nums):
        result = [0 for i in nums]
        prod = 1
        zero = 0
        for n in nums:
            if n != 0:
                prod *= n
            else:
                zero += 1
        if zero > 1:
            return result
        # print(prod)
        left = 1

        right = prod
        for i, n in enumerate(nums):
            if n != 0:
                right = int(right / n)
            # print(f"{left} {right}")
                if zero > 0:
                    result[i] = 0
                else:
                    result[i] = left * right
            else:
                result[i] = left * right
            left *= n
        # print(result)
        return result
print(Solution().productExceptSelf([-1,1,0,-3,3]))
print(Solution().productExceptSelf([1, 2, 3, 4]))
print(Solution().productExceptSelf([0,2,3,4]))
print(Solution().productExceptSelf([0,4,0]))
