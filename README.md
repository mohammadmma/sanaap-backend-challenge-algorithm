# Sanaap Algorithm Challenge
Solutions to algorithm problems for the Sanaap technical challenge.

## Repository Structure
algorithm_challenge/

├── problem-1/

│ ├── first_solution/

│ │ ├── try.py

│ │ ├── clean.py

│ │ └── improve.py

│ ├── pythonic_solution.py

│ └── final_solution.py

│

└── problem-2/

├── first_solution/

│ ├── try.py

│ └── improve.py

├── pythonic_solution.py

└── final_solution.py


## Solutions Overview
Each problem directory contains three solution approaches:

- first_solution/ — Development progression showing the iterative problem-solving process
    - try.py — Initial approach
    - clean.py — Refactored version
    - improve.py — Performance improvements

- pythonic_solution.py — Clean, idiomatic Python implementation focusing on readability

- final_solution.py — Optimized solution with best time/space complexity

## Requirements
- python 3.12

## Problem Descriptions

### Problem 1: Longest Alphabetic Substring

Find the length of the longest substring where:
- Characters are in strictly ascending alphabetical order
- No character repeats

**Example:**
- Input: `"ABCABCFKAB"`
- Output: `5`
- Explanation: The substring `"ABCFK"` has length 5, where each character is greater than the previous one (A < B < C < F < K)

**Edge Cases:**
- Single character strings return 1
- Strings with no ascending sequences return 1
- Case sensitivity **doesn't** matter

### Problem 2: Four Consecutive Ones (Circular)

Determine if a binary string contains four consecutive `1`s, considering the string as circular (the end wraps around to the beginning).

**Example 1:**
- Input: `"1010111"`
- Output: `True`
- Explanation: Contains `"1111"` at positions 4-7 (or indices 4,5,6,7 if we consider "0111" + rotation)

**Example 2:**
- Input: `"11011011"`
- Output: `True`
- Explanation: When treated as circular, the last three `1`s (`"...11"`) connect with the first `1` (`"1..."`) to form `"1111"`

**Edge Cases:**
- Strings shorter than 4 characters return False
- Must handle wrap-around at string boundaries
- Only binary strings (0s and 1s) are valid input


### Approach
1. Initial solution — Focus on correctness
2. Refactoring — Improve code clarity and structure
3. Optimization — Enhance performance and reduce complexity
4. Pythonic version — Leverage Python idioms for clean, readable code
5. Final solution — Balance between readability and performance

## Solutions Complexities

### Problem 1
- Time Complexity --> O(N)
- Space Complexity --> O(1)

### Problem 2
- Time Complexity --> O(N)
- Space Complexity --> O(1)
