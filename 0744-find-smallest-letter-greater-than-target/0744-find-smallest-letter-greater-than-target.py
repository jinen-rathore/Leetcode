class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # using linear search
        # for char in letters:
        #     if ord(char) > ord(target):
        #         return char
        # return letters[0]
        
        # since letters is sorted: we can use binary search
        
        if target >= letters[-1] or target < letters[0]:
            return letters[0]
        
        l,r = 0,len(letters) - 1
        while l <= r:
            m = (l + r) // 2
            if target >= letters[m]:
                l = m + 1
            else:
                r = m - 1
        return letters[l]
                