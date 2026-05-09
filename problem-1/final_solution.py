string = input("enter your string here: ")



def find_longest_len(string: str) -> int:
    if not string:
        return 0
        
    longest_len = 1
    length = 1
    
    for i in range(len(string) - 1):
        if string[i].lower() < string[i+1].lower():
            length += 1
        else:
            longest_len = max(longest_len, length)
            length = 1
            
    return max(longest_len, length)

print(f"longest = {find_longest_len(string)}")
