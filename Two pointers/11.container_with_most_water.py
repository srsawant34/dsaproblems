class Solution:
    def maxArea(self, height: List[int]) -> int:
        low = 0
        high = len(height)-1
        volume = 0
        while low<high:
            lowest_height = min(height[low],height[high])
            vol = (high-low)*lowest_height
            if height[low]==lowest_height:
                low+=1
            else:
                high-=1
            print(vol)
            volume = max(volume,vol)
        return volume