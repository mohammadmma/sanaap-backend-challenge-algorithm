string = input("enter your string here: ")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def find_longest_len(string:str) -> int:
    string = string.lower()
    length = 1
    longest_len = 0

    for i in range(len(string)):
        try:
            current_char = string[i]
            next_char = string[i+1]

            if alphabet.index(current_char) < alphabet.index(next_char):
                length += 1
            else:
                if length > longest_len:
                    longest_len = length
                length = 1

        except IndexError as e:
            continue

    return longest_len
        
print(f"longest = {find_longest_len(string)}")

