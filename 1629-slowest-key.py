class Solution:
    def slowestKey(self, releaseTimes, keysPressed):
        timings = dict()
        base_time = 0
        for i in range(len(releaseTimes)):
            new_time = releaseTimes[i] - base_time
            base_time = releaseTimes[i]
            if keysPressed[i] in timings:
                if new_time > timings[keysPressed[i]]:
                    timings[keysPressed[i]] = new_time
            else:
                timings[keysPressed[i]] = new_time


        final_list = sorted(timings.items(), key=lambda x: x[1], reverse=True)
        top_item = final_list[0][1]
        return_list = []
        for i in final_list:
            if i[1] == top_item:
                return_list.append(i[0])
        # return_list =  [ i if i[1] > top_item   else breal]
        return sorted(return_list)[-1]


Solution().slowestKey([9,29,49,50], "cbcd")

