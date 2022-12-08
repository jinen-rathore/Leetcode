class Solution:
    def maxArea(self, height: List[int]) -> int:
        sum = 0
        i=0 
        j = len(height)-1
        l = len(height)

        while(i < j):

            if(height[i] < height[j]):
                sum = max(sum,height[i]*(j-i))
                i+=1
            else:
                sum = max(sum,height[j]*(j-i))
                j-=1
        return sum

            