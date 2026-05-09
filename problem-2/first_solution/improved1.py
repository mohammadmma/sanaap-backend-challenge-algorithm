binray_string = input("enter your binary string here: ")

def check_four_one(string: str) -> bool:
    if len(string) < 4:
        return False

    concat = string + string[0:3]
    count = 0
    
    for b in concat:
        if b == '1':
            count += 1
            if count == 4:
                return True
        else:
            count = 0
            
    return False

print(check_four_one(binray_string))