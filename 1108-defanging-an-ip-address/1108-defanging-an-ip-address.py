class Solution:
    def defangIPaddr(self, address: str) -> str:
        sl = address.split(".")
        return "[.]".join(sl)
        