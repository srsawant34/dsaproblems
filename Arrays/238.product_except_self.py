class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_till_now = 1
        ans = [1 for i in range(len(nums))]
        for i in range(len(nums)):
            ans[i] = left_till_now
            left_till_now *= nums[i]
        
        right_till_now = 1
        for i in range(len(nums)-1,-1,-1):
            ans[i] = right_till_now*ans[i]
            right_till_now*=nums[i]
        # ans[0]*=right_till_now
        return ans