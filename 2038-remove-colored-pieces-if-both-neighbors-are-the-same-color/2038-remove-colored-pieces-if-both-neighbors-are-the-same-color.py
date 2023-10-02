class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        countA, countB = 0, 0
        # we just check the count of occuring triplets of AAA and BBB
        for i in range(1, len(colors) - 1):
            if colors[i] == "A" and colors[i-1] == "A" and colors[i+1] == "A":
                countA += 1
            
            if colors[i] == "B" and colors[i-1] == "B" and colors[i+1] == "B":
                countB += 1
                
        # if the chances of alice is greater than bob
        # alice will win
        # if the chances of bob are greater than alice, bob will win
        # if there are equal chances then as alice is starting first
        # bob will win
        return countA - countB >= 1
        
            