class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0
        for i in range(len(arr)):
            temp = []
            for j in range(i, len(arr)):
                temp.append(arr[j])
                if len(temp) % 2 != 0:
                    res += sum(temp)
        return res