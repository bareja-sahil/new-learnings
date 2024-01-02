import sys


def min_elements(nums, target):
    target_map = {}

    def recurse(nums, target):
        if target in target_map:
            return target_map[target]
        if target == 0:
            return 0
        if target < 0:
            return sys.maxsize
        min_ans = sys.maxsize
        for num in nums:
            ans = recurse(nums, target-num)
            if ans != sys.maxsize:
                min_ans = min(1+ans, min_ans)
        target_map[target] = min_ans
        return min_ans
    return recurse(nums, target)
from timeit import default_timer as timer

start = timer()
print(min_elements([1, 2, 3], 3))
end = timer()
print(end - start)

