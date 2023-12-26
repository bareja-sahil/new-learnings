class Solution:

    @staticmethod
    def combination_sum(candidates, target):
        combo = []

        def result(idx, curr, capcity):
            if target == capcity:
                combo.append(curr.copy())
                return
            if idx >= len(candidates) or capcity > target:
                return

            curr.append(candidates[idx])
            result(idx, curr, capcity + candidates[idx])
            curr.pop()
            result(idx+1, curr, capcity)

                # if response1 and response2:
                #     return [[candidates[idx]] + option1, [candidates[idx]] + option2], True
                # if response1 is False:
                #     if response2 is False:
                #         return [], False
                #     else:
                #         return option2, response2
                # else:
                #     return [candidates[idx]] + option1, True
        result(0, [], 0)
        print(combo)



x = [2,3,5]
sum = 8
print(Solution.combination_sum(x, sum))
# for s in range(len(x)):
#     print()