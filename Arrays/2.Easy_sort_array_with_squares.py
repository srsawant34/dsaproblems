#https://www.interviewbit.com/problems/sort-array-with-squares/
"""
  Write a function that takes in a non-empty array of integers that are sorted
  in ascending order and returns a new array of the same length with the squares
  of the original integers also sorted in ascending order.
"""


def sortedSquaredArray(array):
    # Write your code here.
    # 1.
    # O(NlogN) Time | O(N) space
    # return sorted([i*i for i in array])

    # 2.
    # O(N) Time | O(N) space
    smallidx = 0
    largeidx = len(array) - 1
    soln = [0 for _ in array]

    for i in range(len(array) - 1, -1, -1):
        smallnum = array[smallidx]
        largenum = array[largeidx]

        if abs(smallnum) > abs(largenum):
            soln[i] = smallnum * smallnum
            smallidx += 1
        else:
            soln[i] = largenum * largenum
            largeidx -= 1
    return soln


input = [1, 2, 3, 5, 6, 8, 9]
expected = [1, 4, 9, 25, 36, 64, 81]
print(expected == sortedSquaredArray(input))