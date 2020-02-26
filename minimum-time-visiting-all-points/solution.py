class Solution:
    def minTimeToVisitAllPoints(self, points):
        x = points[0][0]
        y = points[0][1]

        steps = 0

        for i in range(1, len(points), 1):
            nextX = points[i][0]
            nextY = points[i][1]

            steps += max(abs(nextX - x), abs(nextY-y))

            x = nextX
            y = nextY

        return steps