def countOdds( low: int, high: int) -> int:
    if (high - low + 1) % 2 ==0:
        return (high - low + 1) // 2
    else:
        if low % 2 == 0:
            return (high - low) // 2
        else:
            return (high - low ) //2 + 1

print(countOdds(3,7))
print(countOdds(8,10))
print(countOdds(1,10))
print(countOdds(800445804,979430543))


        