'''
we are supposed to create an empty list where will input all consecutive sequence numbers as they appear in the list.
we will have to loop through the list
do we need pointers?
we need to then count the total number of numbers that follow each other.
if the list is empty, it means we didn't see any consecutive number and it returns zero
the numbers in the list do not have to be next to each other.
we are looking for the longest number of distinct intergers that follow each other without a gap.
idntify where the sequence begins and ends
we also have to count the length of each sequence.
we used a for loop to find where each sequence begins. <it examines each unique number in the set, one after another.
it is asking "the number that preceds it, does it exist? 
the for loop is therefore responsible for searching the set for possible starting points.
once the for loop finds a starting point, the while loop takes over. it count how long each sequence is.
The while loop continues while the next number exists. It stops when it looks for 5 and discovers that 5 is absent.
'''

def longest_consecutive(numbers):
    if  not numbers:
        return 0
    
    number_set = set(numbers)
    longest_length = 1
    
    for num in number_set:
        if num - 1 not in number_set:
            current = num
            current_length = 1
            while current + 1 in number_set:
                current += 1
                current_length += 1
                if current_length > longest_length:
                    longest_length = current_length
    return longest_length

'''
# Longest Consecutive Sequence

## Problem
Given a list of numbers, return the length of the longest sequence of consecutive integers.

The numbers do not need to appear next to each other in the original list.

## Function Signature
`longest_consecutive(numbers) -> int`

## Examples
| input | output | why |
|---|---|---|
| `[100, 4, 200, 1, 3, 2]` | `4` | the sequence `1, 2, 3, 4` has length 4 |
| `[1, 2, 3, 4, 5]` | `5` | the entire list forms a consecutive sequence |
| `[10, 30, 20]` | `1` | no two numbers are consecutive; longest streak is 1 |
| `[1, 1, 2, 2, 3]` | `3` | duplicates count once; sequence is `1, 2, 3` |
| `[9, 1, 4, 7, 3, 2, 6, 5]` | `7` | sequence is `1, 2, 3, 4, 5, 6, 7` |
| `[-3, -2, -1, 1, 2]` | `3` | sequence is `-3, -2, -1` (0 is missing to connect to 1, 2) |
| `[5]` | `1` | single element has streak length 1 |
| `[]` | `0` | empty list has streak length 0 |

## Requirements
To complete this drill, your solution must pass both parts:
1. **Part 1 — Correctness**:
   - return the length of the longest consecutive sequence
   - return `0` if the list is empty
   - do not count duplicate numbers more than once
   - do not modify the original list
2. **Part 2 — Algorithmic Efficiency**:
   - **Time complexity:** average $O(n)$ time.
   - **Constraint:** do not sort the list (`sorted` and `.sort()` are `O(n log n)`). Achieve average $O(n)$ time using a set lookup approach.

## Assumptions
- numbers are integers (positive, negative, or zero)
- original order does not matter
- empty list returns `0`
- do not mutate the input list

## Hint
Start by solving Part 1 using sorting (`sorted()`) to understand the problem and get all test cases to pass.

Once Part 1 passes, refactor for Part 2 using a **set** to get $O(n)$ time without sorting:
- Inserting all numbers into a `set` gives $O(1)$ average lookups.
- *The key efficiency insight:* When iterating through your set, how do you know if a number is the **beginning** of a streak? If `num - 1` is already in the set, should you start counting from `num`, or skip it and let its streak be counted from its true beginning?

'''