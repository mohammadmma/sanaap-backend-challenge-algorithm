binray_string = input("enter your binary string here: ")

def check_four_one(string: str) -> bool:
    n = len(string)
    if n < 4:
        return False

    count = 0
    for i in range(n + 3):
        if string[i % n] == '1':
            count += 1
            if count == 4:
                return True
        else:
            count = 0
            
    return False

print(check_four_one(binray_string))