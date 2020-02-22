class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        
        return self.recurse(rowIndex, 2, [1,1])
    
    def recurse(self, targetIndex, currIndex, prevRow):
        if currIndex > targetIndex:
            return prevRow
        
        currRow = [0] * (currIndex + 1)
        for i in range(len(currRow)):
            if i == 0 or i == len(currRow) - 1:
                currRow[i] = 1
            else:
                currRow[i] = prevRow[i -1] + prevRow[i]
        
        return self.recurse(targetIndex, currIndex + 1, currRow)