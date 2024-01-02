class Solution:
    phone_map = {
        2: 'abc',
        3: 'def',
        4: 'ghi',
        5: 'jkl',
        6: 'mno',
        7: 'pqrs',
        8: 'tuv',
        9: 'wxyz',
    }
    results = []
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return self.results
        def recur(digits, i, result):
            if len(result) == len(digits):
                self.results.append(result)
                return
            value = self.phone_map[int(digits[i])]
            for v in value:
                recur(digits, i+1, result+v)
        recur(digits, 0, '')
        return self.results

print(Solution().letterCombinations('23'))