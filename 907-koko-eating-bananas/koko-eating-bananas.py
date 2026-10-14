class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r
        while l<=r:
            k = (l+r) // 2
            totaltime = 0
            for pile in piles:
                totaltime += math.ceil(pile / k)
            if totaltime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res
