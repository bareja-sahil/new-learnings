import sys

memo_dict = {}


def egg_floor_recursion(eggs, floors):
    key = (eggs, floors)
    if key in memo_dict:
        return memo_dict[key]
    if eggs == 1:
        memo_dict[key] = floors
        return floors
    if floors == 0 or floors == 1:
        memo_dict[key] = floors
        return floors
    minimum_floors = sys.maxsize
    for floor in range(1, floors+1):
        res = 1 + max(egg_floor_recursion(eggs-1, floor-1), egg_floor_recursion(eggs, floors-floor))
        if res < minimum_floors:
            minimum_floors = res
    memo_dict[key] = minimum_floors
    return minimum_floors

print(egg_floor_recursion(2, 100))