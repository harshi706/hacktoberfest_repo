class Solution:
    def minBitFlips(self, start, goal):
        count = 0
        n = start ^ goal
        while n > 0:
            if n & 1 == 1:
                count += 1
            n = n >> 1
        return count
