import random
class RandomizedSet:
    # one method is using the set() in python
    def __init__(self):
        self.s = set()
        self.d = dict()

    def insert(self, val: int) -> bool:
        # this is the basic set fucntion uisng python
        
        if val not in self.s:
            self.s.add(val)
            return True
        return False
    
    def remove(self, val: int) -> bool:        
        if val in self.s:
            self.s.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        ind = random.randint(0, len(self.s)-1)
        return list(self.s)[ind]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()