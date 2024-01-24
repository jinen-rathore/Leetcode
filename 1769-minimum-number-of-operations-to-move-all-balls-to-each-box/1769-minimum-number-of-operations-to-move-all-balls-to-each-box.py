class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # res = [0] * len(boxes)
        # arr = []
        # for i, ele in enumerate(boxes):
        #     if ele == "1":
        #         arr.append(i)
        # print(arr)
        # for i in range(len(boxes)):
        #     temp = 0
        #     for j in range(len(arr)):
        #         temp += abs(i-arr[j])
        #     res[i] = temp
        # return res
        
        n = len(boxes)
        ans = [0] * n
        
        leftCount, leftCost, rightCount, rightCost = 0,0,0,0
        
        for i in range(1, n):
            if boxes[i-1] == "1":
                leftCount += 1
            leftCost += leftCount
            ans[i] = leftCost
        
        for i in range(n-2, -1, -1):
            if boxes[i+1] == "1":
                rightCount += 1
            rightCost += rightCount
            ans[i] += rightCost
        return ans