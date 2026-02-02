#Exponent Function

print(2**4)
#didnt get thid code gonna come back and try to understand
def raise_power(base_num,pow_num):
    result = 1
    for i in range(pow_num):
        result = result *base_num
    return result

print(raise_power(4,5))