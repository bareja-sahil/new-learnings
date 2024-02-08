def solve(target, speed, positions):
    ext_stack = []
    target_achieved = 0
    ext_stack.append((positions[0], speed[0]))
    for i in range(1, len(speed)):
        if (ext_stack[-1][0] + ext_stack[-1][1]) > target:
            ext_stack.append((positions[i], speed[i]))
            continue
        last = ext_stack.pop()
        last_distance = last[0] + last[1]
        current_distance = positions[i] + speed[i]
        if (speed[i] == last[1]) and (positions[i] != last[0]):
            ext_stack.append(last)
            ext_stack.append((positions[i], speed[i]))
        elif (abs(last_distance-current_distance) % min(last[1], speed[i])) == 0:
            max_distance = max(last_distance, current_distance)
            min_speed = min(last[1], speed[i])

            ext_stack.append((max_distance, min_speed))
        else:
            ext_stack.append(last)
            ext_stack.append((positions[i], speed[i]))
    print(ext_stack)

solve(12, [2 ,4 , 1, 1, 3], [10, 8, 0, 5, 3])
solve(10, [3], [3])
solve(100,  [4, 2, 1], [0, 2, 4])




