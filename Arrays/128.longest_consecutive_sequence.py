class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashh = {}
        if nums==[]:
            return 0
        for i in nums:
            hashh[i]=1
        print(hashh)
        maxl = 0
        for i in range(len(nums)):
            if nums[i]+1 not in hashh:
                l = nums[i]
                while l-1 in hashh:
                    hashh[l-1] = hashh[l]+1
                    l-=1
        return max(hashh.values())