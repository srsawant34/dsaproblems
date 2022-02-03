"""
  Write a function that takes in a non-empty array of distinct integers and an
  integer representing a target sum. If any two numbers in the input array sum
  up to the target sum, the function should return them in an array, in any
  order. If no two numbers sum up to the target sum, the function should return
  an empty array.
  Note that the target sum has to be obtained by summing two different integers
  in the array; you can't add a single integer to itself in order to obtain the
  target sum.
  You can assume that there will be at most one pair of numbers summing up to
  the target sum.
  array = [3, 5, -4, 8, 11, 1, -1, 6]
  targetSum = 10
  Sample Output: [-1, 11] // the numbers could be in reverse order
"""

# key idea: hash map

def twoNumberSum(array, targetSum):
    # Write your code here
    '''
    # 1.
    # O(n) Time | O(n) Space
    arrhash={}
    for num in array:
        diff = targetSum - num
        if diff in arrhash:
            return [diff,num]
        else:
            arrhash[num] = True
    return []
    '''

    # 2.
    # O(NlogN) because of sort(), the while loop is of O(N)| O(1) Space
    array.sort()
    left = 0
    right = len(array) - 1

    while left < right:
        currSum = array[left] + array[right]
        if currSum == targetSum:
            return [array[left], array[right]]
        elif currSum < targetSum:
            left += 1
        elif currSum > targetSum:
            right -= 1
    return []


array = [-21, 301, 12, 4, 65, 56, 210, 356, 9, -47]
targetSum = 163
print(twoNumberSum(array, targetSum))