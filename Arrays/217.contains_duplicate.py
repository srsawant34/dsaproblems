class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict_nums = {}
        for i in nums:
            if i in dict_nums:
                return 1
            else:
                dict_nums[i] = 1
        return 0
