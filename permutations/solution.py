'''

This algorithm has the goal of printing out all permutations of an arry (python --> list).

The main method being used is backtracking (a form of DFS), which focuses on building up from each value.
The use of recursion is to make sure that all path ways are taken and when exhausted backtracks.

In this specific algorithm, all items in the array are unique and distinct (one of each);
So our algorithm only has to deal with one character at a time and not be required to use
another data structure to keep track (flagging method).

Usually, backtracking requires another data strucutre for a flagging method (keep track of visited items).
Lists or dictionarys are often used to keep track of visited items.

'''

class Solution:
    
    def permute(self, arr):
        output = []
        self.backtrack(arr, [], output)
        return output

    def backtrack(self, arr, out, output):
        if len(out) == len(arr):
            output.append(out[:])
        else:
            for num in arr:
                # condition of choices
                if num in out: continue

                # make choice
                out.append(num)

                # step into choice
                self.backtrack(arr, out, output)

                # undo choice
                out.pop()

    # use of data structure to keep track, in this case python's hashset(), which can only store unique values

class Solution2:
    
    def permute(self, arr):
        res = []
        self.backtrack(arr, [], set(), res)
        return res

    def backtrack(self, arr, temp, visited, res):
        if len(temp) == len(arr):
            res.append(temp[:])
        else:
            for num in arr:
                # condition of choice
                if num in visited: continue

                # make choice
                visited.add(num)
                temp.append(num)

                # step into
                self.backtrack(arr, temp, visited, res)
                
                # undo our actions
                visited.remove(num)
                temp.pop()