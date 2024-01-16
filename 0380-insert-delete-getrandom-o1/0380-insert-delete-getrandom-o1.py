import random
class RandomizedSet:

    def __init__(self):
        # self.hm = {}
        self.s = set()

    def insert(self, val: int) -> bool:
        # if val not in self.hm:
        #     self.hm[val] = 1
        #     return True
        # else:
        #     self.hm[val] += 1
        #     return False
        
        if val not in self.s:
            self.s.add(val)
            return True
        return False
    
    def remove(self, val: int) -> bool:
        # if val in self.hm and self.hm[val] > 1:
        #     self.hm[val] -= 1
        #     return True
        # elif val in self.hm and self.hm[val] == 1:
        #     self.hm.pop(val)
        #     return True
        # else:
        #     return False
        
        if val in self.s:
            self.s.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        # key, val = random.choice(list(self.hm.items()))
        # return key
        
        ind = random.randint(0, len(self.s)-1)
        return list(self.s)[ind]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()