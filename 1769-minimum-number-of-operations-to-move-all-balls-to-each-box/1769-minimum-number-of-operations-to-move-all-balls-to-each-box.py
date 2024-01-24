class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = [0] * len(boxes)
        arr = []
        for i, ele in enumerate(boxes):
            if ele == "1":
                arr.append(i)
        print(arr)
        for i in range(len(boxes)):
            temp = 0
            for j in range(len(arr)):
                temp += abs(i-arr[j])
            res[i] = temp
        return res