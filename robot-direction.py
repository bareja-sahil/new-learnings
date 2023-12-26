class Solution:
    def isRobotBounded(self, instructions):
        axis = [0, 0]
        x = ['E', 'W']
        y = ['N', 'S']
        current_direction = 'N'
        keyword = {
            'N': 1,
            'S': -1,
            'E': 1,
            'W': -1
        }
        # Left, right
        keyword2 = {
            'N': ['W', 'E'],
            'S': ['E', 'W'],
            'E': ['N', 'S'],
            'W': ['S', 'N']
        }
        for instrcut in instructions:
            if instrcut == "G":
                if current_direction in x:
                    axis[0] += keyword[current_direction]
                else:
                    axis[1] += keyword[current_direction]
            elif instrcut == 'L':
                current_direction = keyword2[current_direction][0]
            else:
                current_direction = keyword2[current_direction][0]
        if axis[0] == 0 and axis[1] == 0:
            return True
        else:
            return False

print(Solution().isRobotBounded('GLGLGLGL'))
