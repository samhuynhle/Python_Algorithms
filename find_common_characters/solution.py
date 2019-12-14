class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        d = {} 
        for letter in A[0]: 
            d[letter] = d.get(letter, 0) + 1
        for word in A[1:]:
            d2 = d.copy()
            for letter in d2: 
                c = word.count(letter) 
                if c != d[letter]:
                    if c >= 1: 
                        d[letter] = min(c, d[letter])
                    else:
                        del(d[letter])
        out = []
        for letter in d:
            for i in range(d[letter]):
                out.append(letter)
        return out   