class Solution:
    
    def permute(self, arr):
        output = []
        self.backtrack(arr, [], output)
        return output

    def backtrack(self, arr, out, output):
        print(out)
        if len(out) == len(arr):
            output.append(out[:])
        else:
            for num in arr:
                if num in out: continue
                    
                out.append(num)
                self.backtrack(arr, out, output)
                out.pop()