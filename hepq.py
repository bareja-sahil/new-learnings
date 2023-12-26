import heapq


class Solution:
    def maxAverageRatio(self, classes, extraStudents) -> float:
        new_dataset = []
        n = len(classes)
        for i in classes:
            students = i[0]
            total_students = i[1]
            pass_ratio = students / total_students
            new_pass_ratio = (students+1) / (total_students+1)
            impacts = pass_ratio - new_pass_ratio
            heapq.heappush(new_dataset, (impacts, students, total_students))
        while extraStudents > 0:
            _, students, total_students = heapq.heappop(new_dataset)
            students += 1
            total_students += 1
            pass_ratio = students / total_students
            new_pass_ratio = (students+1) / (total_students+1)
            impacts = pass_ratio - new_pass_ratio
            heapq.heappush(new_dataset, (impacts, students, total_students))
            extraStudents -= 1
        result = 0
        for _, students, total_students in new_dataset:
            result += students / total_students
        return result/n

print(Solution().maxAverageRatio([[2,4],[3,9],[4,5],[2,10]], extraStudents=4))
