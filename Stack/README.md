# **Stack**

Easy

1. [20. Valid Parentheses](#20-valid-parentheses)

Medium

2. [155. Min Stack](#155-min-stack)
3. [150. Evaluate Reverse Polish Notation](#150-evaluate-reverse-polish-notation)
4. [22. Generate Parentheses](#22-generate-parentheses)
5. [739. Daily Temperatures](#739-daily-temperatures)
6. [853. Car Fleet](#853-car-fleet)

Hard

7. [84. Largest Rectangle in Histogram](#84-largest-rectangle-in-histogram)

## **Easy**

### **20. Valid Parentheses**

[Leetcode](https://leetcode.com/problems/valid-parentheses/description/) | [file](20.valid_parentheses.py)

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.
 

Example 1:
```
Input: s = "()"
Output: true
```

Example 2:
```
Input: s = "()[]{}"
Output: true
```
Example 3:
```
Input: s = "(]"
Output: false
```

Constraints:

1. `1 <= s.length <= 104`
2. `s` consists of parentheses only `'()[]{}'`.

## **Medium**

### **155. Min Stack**

[Leetcode](https://leetcode.com/problems/min-stack/) | [file](155.min_stack.py)

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the `MinStack` class:

`MinStack()` initializes the stack object.
`void push(int val)` pushes the element val onto the stack.
`void pop()` removes the element on the top of the stack.
`int top()` gets the top element of the stack.
`int getMin()` retrieves the minimum element in the stack.
You must implement a solution with `O(1)` time complexity for each function.

 

Example 1:
```
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
``` 

Constraints:

1. `-231 <= val <= 231 - 1`
2. Methods pop, top and getMin operations will always be called on non-empty stacks.
3. At most `3 * 104` calls will be made to `push`, `pop`, `top`, and `getMin`.

### **150. Evaluate Reverse Polish Notation**

[Leetcode](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | [file](150.reverse_polish_notation.py)

You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are `'+'`, `'-'`, `'*'`, and `'/'`.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

Example 1:
```
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
```
Example 2:
```
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
```
Example 3:
```
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
``` 

Constraints:

1. `1 <= tokens.length <= 104`
2. `tokens[i]` is either an operator: `"+"`,` "-"`, `"*"`, or `"/"`, or an integer in the range `[-200, 200]`.


### **22. Generate Parentheses**

[Leetcode](https://leetcode.com/problems/generate-parentheses/) | [file](22.generate_parantheses.py)

Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
```
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
```

Example 2:
```
Input: n = 1
Output: ["()"]
``` 

Constraints:

- `1 <= n <= 8`

### **739. Daily Temperatures**

[Leetcode](https://leetcode.com/problems/daily-temperatures/) | [file](739.daily_temperature.py)

Given an array of integers `temperatures` represents the daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the `ith` day to get a warmer temperature. If there is no future day for which this is possible, keep `answer[i] == 0` instead.

Example 1:
```
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
```
Example 2:
```
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
```
Example 3:
```
Input: temperatures = [30,60,90]
Output: [1,1,0]
```

Constraints:

1. `1 <= temperatures.length <= 105`
2. `30 <= temperatures[i] <= 100`

### **853. Car Fleet**

[Leetcode](https://leetcode.com/problems/car-fleet/) | [file](853.car_fleet.py)

There are `n` cars going to the same destination along a one-lane road. The destination is `target` miles away.

You are given two integer array `position` and `speed`, both of length `n`, where `position[i]` is the position of the `ith` car and `speed[i]` is the speed of the `ith` car (in miles per hour).

A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed. The faster car will slow down to match the slower car's speed. The distance between these two cars is ignored (i.e., they are assumed to have the same position).

A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

Return the number of car fleets that will arrive at the destination.

 

Example 1:
```
Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation:
The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12.
The car starting at 0 does not catch up to any other car, so it is a fleet by itself.
The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
Note that no other cars meet these fleets before the destination, so the answer is 3.
```
Example 2:
```
Input: target = 10, position = [3], speed = [3]
Output: 1
Explanation: There is only one car, hence there is only one fleet.
```
Example 3:
```
Input: target = 100, position = [0,2,4], speed = [4,2,1]
Output: 1
Explanation:
The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet, meeting each other at 4. The fleet moves at speed 2.
Then, the fleet (speed 2) and the car starting at 4 (speed 1) become one fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
``` 

Constraints:

1. `n == position.length == speed.length`
2. `1 <= n <= 105`
3. `0 < target <= 106`
4. `0 <= position[i] < target`
5. All the values of position are unique.
6. `0 < speed[i] <= 106`

## **Hard**

### **84. Largest Rectangle in Histogram**

[Leetcode](https://leetcode.com/problems/largest-rectangle-in-histogram/) | [file](84.largest_rectangle_histogram.py)

Given an array of integers `heights` representing the histogram's bar height where the width of each bar is `1`, return the area of the largest rectangle in the histogram.

Example 1:

![example1](https://assets.leetcode.com/uploads/2021/01/04/histogram.jpg)
```
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
```
Example 2:

![example2](https://assets.leetcode.com/uploads/2021/01/04/histogram-1.jpg)
```
Input: heights = [2,4]
Output: 4
``` 

Constraints:

1. `1 <= heights.length <= 105`
2. `0 <= heights[i] <= 104`
