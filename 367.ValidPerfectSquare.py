def isPerfectSquare(num:int):
    l , r = 1, 2**16
    while l < r:
        mid =  l + (r - l) // 2
        midSquare = mid * mid
        if midSquare == num:
            return True
        elif midSquare > num:
            r = mid
        else:
            l = mid + 1
    return False

print(isPerfectSquare(16))