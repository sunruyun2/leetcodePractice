def canPlaceFlowers(flowerbed:list[int], n:int)->bool:
    numsOf0 = 1
    flowerbed.append(0)
    for i in range(len(flowerbed)):
        if flowerbed[i] == 1:
            n -= (numsOf0 -1) //2
            numsOf0 = 0
        else:
            numsOf0 +=1
    n -= (numsOf0 -1) //2
    return n <= 0

print(canPlaceFlowers([1,0,0,0,1,0,0],2))