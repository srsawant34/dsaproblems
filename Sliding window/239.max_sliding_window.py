class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()  # index
        l = r = 0
        # O(n) O(n)
        while r < len(nums):
            # pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove left val from window
            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = [nums[0]]
        soln=[]
        print(nums)
        for i in range(1,k):
            while dq !=[] and dq[-1]<nums[i]:
                print(dq)
                dq.pop()
            dq.append(nums[i])
        soln.append(dq[0])
        
        start=0
        for i in range(k,len(nums)):
            while dq!=[] and dq[-1]<nums[i]:
                dq.pop()
            dq.append(nums[i])
            if dq[0]==nums[start]:
                dq.pop(0)
            soln.append(dq[0])
            start+=1
        return soln