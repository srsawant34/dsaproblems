class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        h = len(matrix[0])-1
        i = 0
        for i in range(len(matrix)):
            if matrix[i][l]<=target and matrix[i][h]>=target:
                while (l<=h):
                    idx = (l+h)//2
                    if matrix[i][idx]==target:
                        return True
                    elif matrix[i][idx]<target:
                        l=idx+1
                    else:
                        h = idx-1
        return False