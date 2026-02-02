#If statements and comparisons

def max_num(num,num1,num2):
    if num>num1 and num>num2:
        return num
    elif num1>num and num1>num2:
        return num1
    else:
        return num2

print(max_num(4,2,3))