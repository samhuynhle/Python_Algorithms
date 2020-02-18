class Solution(object):
    def generatePalindromes(self, s):
        if len(s) == 1: return [s]
        counter = collections.Counter(s)
        count = 0
        build = []
        output = []
        for char in counter:
            if counter[char] % 2 != 0:
                count = count + 1
                build.append(char)        
            if count > 1: return []
        
        self.backtrack(build, output, counter, len(s))
        return output
                
    def backtrack(self, build, output, counter, target):
        if len(build) == target:
            output.append("".join(build))
        for char in counter:
            if counter[char] > 1:
                counter[char] -= 2
                self.backtrack([char] + build + [char], output, counter, target)
                counter[char] += 2