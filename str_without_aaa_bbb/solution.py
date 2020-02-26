class Solution(object):
    def strWithout3a3b(self, A, B):
        builder = []

        while A or B:
            if len(builder) >= 2 and builder[-1] == builder[-2]:
                writer = builder[-1] == 'b'
            else: 
                writer = A >= B

            if writer:
                builder.append('a')
                A -= 1
            else:
                builder.append('b')
                B -= 1
            
        return ''.join(builder)