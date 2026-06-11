class Solution:

    def encode(self, strs: List[str]) -> str:
        return "á".join(strs + [""])

    def decode(self, s: str) -> List[str]:
        return s.split("á")[:-1]
