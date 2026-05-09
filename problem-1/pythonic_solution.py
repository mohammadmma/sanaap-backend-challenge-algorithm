from itertools import pairwise


string = input("enter your string here: ")

def find_longest_len_pythonic(string: str) -> int:
    if not string:
        return 0
        
    longest_len = 1
    length = 1
    
    for current_char, next_char in pairwise(string.lower()):
        if current_char < next_char:
            length += 1
        else:
            longest_len = max(longest_len, length) 
            length = 1
            
    return max(longest_len, length)

print(f"longest = {find_longest_len_pythonic(string)}")
