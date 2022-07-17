# 1. intuition - use string
def reverse(x:int)->int:

    # format the integer into string
    if x < 0:
        str_x = '-'+ str(x)[1:][::-1]
    else:
        str_x = str(x)[::-1]

    # in case the integer is 0
    if len(str_x) ==1:
        return x

    # incase the integer end up with 0
    while str_x[0] == "0":
        str_x = str_x[1:]

    # return 0 if the integer is out of range
    if int(str_x) > pow(2,31) or int(str_x) <-1 *(pow(2,31)):
        return 0
    
    return int(str_x)

# print(reverse(3))
# print(reverse(-3))
# print(reverse(-24))
# print(reverse(121434))
# print(reverse(214340))
# print(reverse(1534236496))

# 2.mathematical way
def reverse(n:int):
    return_num = 0
    if n < 0:
        plus_minus = -1
        n = n* -1
    else:
        plus_minus = 1
    while n !=0:
        return_num = return_num * 10
        remainder = n % 10
        return_num +=remainder
        n = n //10

    return_num = return_num * plus_minus
    
    if return_num > pow(2,31) or return_num <-1 *(pow(2,31)):
        return 0
    return return_num

print(reverse(0))
print(reverse(3))
print(reverse(-3))
print(reverse(-24))
print(reverse(121434))
print(reverse(214340))
print(reverse(1534236496))