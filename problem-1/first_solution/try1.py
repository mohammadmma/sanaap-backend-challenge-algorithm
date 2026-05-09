string = input("enter your string here: ")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'y', 'z']

string = string.lower()
length = 1
longest_len = 0


# print(string.index("s"))

for i in range(len(string)):
    # print(i)
    try:
        current_char = string[i]
        next_char = string[i+1]

        if alphabet.index(current_char) < alphabet.index(next_char):
            print(f"niceeeeeeee\tcurrent --> {current_char}, next --> {next_char}, length before add = {length}", end="\t")
            length += 1
            print(f"niceeeeeeee\tcurrent --> {current_char}, next --> {next_char}, length after add = {length}", end="\n\n")
        else:
            if length > longest_len:
                longest_len = length
            print(f"Ooooooooooops\tcurrent --> {current_char}, next --> {next_char}, length before reset = {length}, long = {longest_len}", end="\n\n")
            length = 1
    except IndexError as e:
        print("hello index")
        print("go on")
        continue
    
print(f"longest = {longest_len}")

