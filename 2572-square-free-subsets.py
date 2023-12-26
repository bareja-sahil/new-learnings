class Solution:
    def squareFreeSubsets(self, nums):
        def check_square_divisiblity(num):
            for j in [4, 9, 12, 16, 18, 20, 24, 25, 27, 28]:
                if num % j == 0:
                    return True

            return False

        square_free_number = []
        squared_number = [4, 9, 12, 16, 18, 20, 24, 25, 27, 28]
        new_list = []
        for i in nums:
            if not check_square_divisiblity(i):
                new_list.append(i)
        # sub sets
        end = len(new_list)
        x_list = []
        for start in range(len(new_list)):
            for end in range(start+1, len(new_list)+1):
                x_list.append(new_list[start:end])
        print(new_list)
        print(x_list)
        return len(x_list)


Solution().squareFreeSubsets([3,4,4,5])
