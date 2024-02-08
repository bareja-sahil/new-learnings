def solve(temps):
    temp_stack = []
    result = [0] * len(temps)
    n = len(temps) - 1
    for i in range(n, -1, -1):
        while len(temp_stack) != 0 and temps[i] >= temps[temp_stack[-1]]:
            temp_stack.pop()
        if len(temp_stack) == 0:
            result[i] = 0
        else:
            result[i] = temp_stack[-1] - i
        temp_stack.append(i)
    return result

# print(solve([73, 74, 75, 71, 69, 72, 76, 73]))
print(solve([30, 40, 50, 60]))