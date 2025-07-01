import heapq as hq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        neg_list = [-1*val for val in stones]
        hq.heapify(neg_list)

        while len(neg_list) > 1 and neg_list[0] != 0:
            hq.heappush(neg_list, hq.heappop(neg_list) - hq.heappop(neg_list))
        return -1 * neg_list[0]