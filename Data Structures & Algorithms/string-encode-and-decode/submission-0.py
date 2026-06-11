class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += s + "á"
        return encoded

    def decode(self, s: str) -> List[str]:
        return s.split("á")[:-1]
