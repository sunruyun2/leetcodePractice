# 1.intuition - hash map and list
# update minFre
# update res list
# failed
from cmath import inf


def topKFrequent(nums:list , k) ->list:
    res = []
    count = {}
    minFre = 0
    for n in nums:
        count[n] = count.get(n , 0) + 1
        if count[n] > minFre and n not in res:
            res.append(n)
        if len(res) > k:
            for i in res:
                minFre =  min(minFre , count[i])

            for i in res:
                if count[i] == minFre:
                    res.remove(i)

    return res

print(topKFrequent([1,1,1,2,2,3],2))
print(topKFrequent([1],1))
