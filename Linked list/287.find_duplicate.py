class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow,fast = nums[0],nums[nums[0]]
        while slow!=fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
        ptr1 = nums[0]
        ptr2 = nums[fast]
        while ptr1!=ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]
            
        return ptr1
    