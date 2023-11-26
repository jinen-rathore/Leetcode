class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        val = 0
        for op in operations:
            if op == "++X" or op == "X++":
                val += 1
            elif op == "--X" or op == "X--":
                val -= 1
        return val