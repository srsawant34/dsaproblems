class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        h = len(numbers)-1
        while l<h:
            add = numbers[l] + numbers[h]
            if add == target:
                return [l+1,h+1]
            elif add>target:
                h-=1
            elif add<target:
                l+=1