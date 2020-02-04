from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sLength, pLength = len(s), len(p)
        if sLength < pLength:
            return []
        pCount = Counter(p)
        sCount = Counter()
        output = []
        for i in range(nLength):
            sCount[s[i]] += 1
            if i >= nLength:
                if sCount[s[i - np]] == 1:
                    del sCount[s[i - np]]
                else: 
                    sCount[s[i - np]] -= 1
            if pCount == sCount:
                output.append(i - nLength + 1)
        return output