def boxes_on_truck(box_types, truck_size):

    def solution(idx, remaining_size):
        if idx == len(box_types):
            return 0
        if box_types[idx][0] >= remaining_size:
            return remaining_size * box_types[idx][1]
        test = box_types[idx][0] * box_types[idx][1]
        option1 = test + solution(idx+1, remaining_size-box_types[idx][0])
        option2 = solution(idx + 1, remaining_size)
        return max(option1, option2)
    return solution(0, truck_size)


box_types = [[6,10],[2,5],[4,7],[3,9]]
truck_size = 10
print(boxes_on_truck(box_types, truck_size))