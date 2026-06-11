class Solution:

    def encode(self, strs: List[str]) -> str:
        return '¨'.join(strs) if strs else "__empty__"

    def decode(self, s: str) -> List[str]:
        return s.split('¨') if s != "__empty__" else []
