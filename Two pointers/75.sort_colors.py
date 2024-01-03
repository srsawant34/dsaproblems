class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        """
        Time: O(n) | Space: O(1)
        """

        colors = nums
        red, white, blue = 0, 0, len(colors) - 1
        
        while white <= blue:
            if colors[white] == 0:
                if colors[red] != 0:
                    colors[red], colors[white] = colors[white], colors[red]
                
                white += 1
                red += 1

            elif colors[white] == 1:
                white += 1

            else:
                if colors[blue] != 2:
                    colors[white], colors[blue] = colors[blue], colors[white]

                blue -= 1

        return
