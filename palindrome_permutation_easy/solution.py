class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        hashmap = dict()
        for char in s:
            if char in hashmap:
                hashmap[char] += 1
            else:
                hashmap[char] = 1
        
        odds = []
        
        for key in hashmap:
            if hashmap[key] % 2 == 1:
                odds.append(hashmap[key])
                if len(odds) > 1:
                    return False
                
        return True