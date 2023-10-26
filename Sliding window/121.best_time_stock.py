class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_so_far = 0
        l = 0
        h = 1
        while l<len(prices)-1 and h<len(prices):
            if prices[l]<prices[h]:
                max_so_far = max(max_so_far, prices[h]-prices[l])
                h+=1
            else:
                l+=1
                h=l+1
        return max_so_far