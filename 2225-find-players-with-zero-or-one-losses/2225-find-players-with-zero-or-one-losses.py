class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        h = {}
        for w, l in matches:
            # creating a hash map list this:
            # h = {1:[1,0], 2:[2,2]}
            # where it denotes the won and loss of the player
            
            if w not in h:
                h[w] = [1,0]
            else:
                h[w][0] += 1
                
            if l not in h:
                h[l] = [0,1]
            else:
                h[l][1] += 1
                
        loss0 = []
        loss1 = []
        
        for key, val in h.items():
            if val[1] == 0:
                loss0.append(key)
            if val[1] == 1:
                loss1.append(key)
        return [sorted(loss0),sorted(loss1)]
        
            