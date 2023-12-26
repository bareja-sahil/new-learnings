class Solution:
    def lengthOfLongestSubstring(self, s: str):

        result = dict()
        alpha = dict()
        start = 0
        end = 0
        main_len = 0
        print(f"xx  {len(s)}")
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        for i in range(len(s)):
            if s[i] == " ":
                print("xx")
                data = "xx"
            else:
                data = s[i]
            x = alpha.get(data, None)
            if x is None:
                end += 1
                main_len += 1
                alpha[data] = 1
            else:
                result[(start, i - 1)] = main_len
                main_len = 1
                start, end = i, i
                alpha = dict()
                alpha[data] = 1
        result[(start, i)] = main_len
        print(result)
        sorted_result = dict(sorted(result.items(), reverse=True, key=lambda x: x[1]))
        for i in sorted_result.items():
            return i[1]
Solution().lengthOfLongestSubstring("xcceeau")