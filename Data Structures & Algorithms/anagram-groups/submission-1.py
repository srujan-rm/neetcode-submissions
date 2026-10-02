class Solution:
    def representation(self, sample: str) -> str:
        hash = [0] * 26 
        for i in sample: 
            hash[ord(i) - ord('a')] += 1 
        for i in range(26):
            hash[i] = str(hash[i])
        return("/".join(hash))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = dict()
        for i in strs: 
            obtained = self.representation(i)
            if (obtained not in hash):
                hash[obtained] = [i]
            else:
                hash[obtained].append(i)
        solution = []
        for v in hash.values():
            solution.append(v)
        return solution