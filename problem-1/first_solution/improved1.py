string = input("enter your string here: ")


def find_longest_len(string:str) -> int:
    string = string.lower()
    length = 1
    longest_len = 1

    for i in range(len(string) - 1):
        current_char = string[i]
        next_char = string[i+1]

        if current_char < next_char:
            length += 1
        else:
            if length > longest_len:
                longest_len = length
            length = 1

    if length > longest_len:
        longest_len = length

    return longest_len
        
print(f"longest = {find_longest_len(string)}")

