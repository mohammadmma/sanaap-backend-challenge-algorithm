binray_string = input("enter your binary string here: ")

def check_four_one_pythonic(string: str) -> bool:
    if len(string) < 4:
        return False
        
    concat = string + string[0:3]
    
    if "1111" in concat:
        return True
    else:
        return False
    

print(check_four_one_pythonic(binray_string))