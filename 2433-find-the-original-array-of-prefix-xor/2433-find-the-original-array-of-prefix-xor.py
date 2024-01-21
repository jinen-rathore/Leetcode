class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        arr = [-1] * len(pref)
        arr[0] = pref[0]
        
        for i in range(1, len(pref)):
            arr[i] = pref[i-1] ^ pref[i]
        return arr
    
        # n = len(pref)
        # for i in range(n-1, 0, -1):
        #     pref[i] = pref[i] ^ pref[i-1]
        # return pref