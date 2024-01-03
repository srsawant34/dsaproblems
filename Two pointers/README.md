# **Two Pointers**

The Two Pointers pattern involves using two pointers to traverse an array or list until specific conditions are met. This approach enables simultaneous tracking of values at two different indexes during a single iteration.

## Pattern
- Input data is processed `linearly`, such as in an array, linked list, or string of characters.
- The Two Pointers pattern narrows attention to a specific range of elements indicated by the positions of two pointers.
- Common tasks in this pattern may include `comparing` or `swapping` values at the two pointers. Each pointer may also traverse a separate array or string.

## Problems

Easy
1. [125. Valid Palindrome](#125-Valid-Palindrome)
2. [680. Valid Palindrome II](#680-Valid-Palindrome-II)

Medium

3. [75. Sort Colors](#75-sort-colors)
4. [19. Remove Nth Node From End of List](#19-remove-nth-node-from-end-of-list)
5. [167. Two Sum II - Input Array Is Sorted](#167-two-sum-ii---input-array-is-sorted)
6. [15. 3Sum](#15-3sum)
7. [11. Container With Most Water](#11-container-with-most-water)

Hard

8. [42. Trapping Rain Water](#42-trapping-rain-water)

## **Easy**

### **125. Valid Palindrome**

[LeetCode](https://leetcode.com/problems/valid-palindrome/) | [file](125.valid_palindrome.py)

A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` *if it is a **palindrome**, or* `false` *otherwise*.

**Example 1:**

```
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
```

### **680. Valid Palindrome II**

[LeetCode](https://leetcode.com/problems/valid-palindrome-ii/) | [file](680.valid_palindrome_II.py)

Given a string `s`, return `true` if the `s` can be palindrome after deleting at most one character from it.

Example 1:
```
Input: s = "aba"
Output: true
```
Example 2:
```
Input: s = "abca"
Output: true
```
Explanation: You could delete the character 'c'.

Example 3:
```
Input: s = "abc"
Output: false
```

Constraints:

1. `1 <= s.length <= 105`
2. `s` consists of lowercase English letters.

## **Medium**

### **75. Sort Colors**

[LeetCode](https://leetcode.com/problems/sort-colors/) | [file](75.sort_colors.py)

Given an array `nums` with `n`` objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers `0`, `1`, and `2` to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:
```
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
```

Example 2:
```
Input: nums = [2,0,1]
Output: [0,1,2]
```

Constraints:
1. `n == nums.length`
2. `1 <= n <= 300`
3. `nums[i]` is either `0`, `1`, or `2`.

### 19. Remove Nth Node From End of List

[Leetcode](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | [file](19.remove_nth_node_end.py)

Given the `head` of a linked list, remove the `nth` node from the end of the list and return its head.

 

Example 1:

![example1](https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg)
```
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
```
Example 2:
```
Input: head = [1], n = 1
Output: []
```
Example 3:
```
Input: head = [1,2], n = 1
Output: [1]
``` 

Constraints:

- The number of nodes in the list is `sz`.
- `1 <= sz <= 30`
- `0 <= Node.val <= 100`
- `1 <= n <= sz`

### **167. Two Sum II - Input Array Is Sorted**

[LeetCode](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | [file](167.two_sum_II.py)

Given a **1-indexed** array of integers `numbers` that is already ***sorted in non-decreasing order***, find two numbers such that they add up to a specific `target` number. Let these two numbers be `numbers[index1]` and `numbers[index2]` where `1 <= index1 < index2 <= numbers.length`.

Return *the indices of the two numbers,* `index1` *and* `index2`*, **added by one** as an integer array* `[index1, index2]` *of length 2.*

The tests are generated such that there is **exactly one solution**. You **may not** use the same element twice.

Your solution must use only constant extra space.

**Example 1:**

```
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
```

**Example 2:**

```
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
```
    

### **15. 3Sum**

[LeetCode](https://leetcode.com/problems/3sum/) | [file](15.three_sum.py)

Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

**Example 1:**

```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
```


### **11. Container With Most Water**

[LeetCode](https://leetcode.com/problems/container-with-most-water/) | [file](11.container_with_most_water.py)

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return *the maximum amount of water a container can store*.

**Notice** that you may not slant the container.

**Example 1:**

![https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg)

```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
```

**Example 2:**

```
Input: height = [1,1]
Output: 1
```

## **Hard**

### **42. Trapping Rain Water**

[LeetCode](https://leetcode.com/problems/trapping-rain-water/) | [file](42.trapping_rain_water.py)

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

**Example 1:**

![https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png](https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png)

```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
```

**Example 2:**

```
Input: height = [4,2,0,3,2,5]
Output: 9
```
