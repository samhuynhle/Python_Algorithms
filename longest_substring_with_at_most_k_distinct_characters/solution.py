from collections import Counter

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        counter = Counter()
        result = 0
        i = 0
        n = 0

        for index, char in enumerate(s):
            if counter[char] == 0: # haven't been seen before
                n += 1
            counter[char] += 1
            while n > k:
                counter[s[i]] -= 1
                if counter[s[i]] == 0:
                    n -= 1
                i += 1
            result = max(result, index - i + 1)
        return result