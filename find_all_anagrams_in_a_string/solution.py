from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sLength, pLength = len(s), len(p)
        if sLength < pLength:
            return []
        pCount = Counter(p)
        sCount = Counter()
        return generateOutput(s, p, sLength, pLength, sCount, pCount)

    def generateOutput(s, p, sLength, pLength, sCount, pCount):
        output = []
        for i in range(sLength):
            sCount[s[i]] += 1
            if i >= sLength:
                if sCount[s[i-pLength]] == 1:
                    del sCount[s[i - pLength]]
                else:
                    sCount[s[i - pLength]] -= 1
            if pCount == sCount:
                output.append(i - sLength + 1)
        return output