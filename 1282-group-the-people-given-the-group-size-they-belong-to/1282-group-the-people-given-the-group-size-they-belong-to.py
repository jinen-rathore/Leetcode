class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        res, hashmap = [], {}
        
        for i, size in enumerate(groupSizes):
            if size not in hashmap:
                hashmap[size] = []
            hashmap[size].append(i)
            
            if len(hashmap[size]) == size:
                res.append(hashmap[size])
                hashmap[size] = []
        return res