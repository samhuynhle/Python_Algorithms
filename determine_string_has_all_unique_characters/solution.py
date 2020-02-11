class Solution:
    def isUnique1(str):
        hashset = set(str)

        if len(hashset) == len(str):
            return True
        else:
            return False

    string = "sam iI "
    print(isUnique1(string))