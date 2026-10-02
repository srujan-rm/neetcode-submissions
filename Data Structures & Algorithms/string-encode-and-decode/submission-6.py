from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        if (len(strs) == 0):
            return "ñ"
        return "π".join(strs)

    def decode(self, s: str) -> List[str]:
        if (s == "ñ"):
            return []
        return s.split("π")
