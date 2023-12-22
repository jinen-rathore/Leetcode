class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # binary addition:
        # 0 + 0 = 1
        # 1 + 0 or 0 + 1 = 1
        # 1 + 1 = 10
        
        add_str = ""
        
        return bin(int(a, 2) + int(b, 2)).replace("0b", "")