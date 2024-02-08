def largest_hist(heights):
    start = 0
    end = len(heights) - 1
    max_hist = 0
    while start <= end:
        hist = min(heights[start], heights[end]) * ((end - start))
        # print(nums[start], nums[end])
        # print(end - start)
        # print(hist)
        max_hist = max(max_hist, hist)
        if end > 0 and heights[end] < heights[end-1]:
            end -= 1
        start += 1
    return max_hist

print(largest_hist([2,4]))