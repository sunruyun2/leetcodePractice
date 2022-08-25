# 1.intuition
# I dont understand the purpose of this problem
def calPoints(ops:list[str])->int:
    res = []
    for op in ops:
        try:
            op = int(op)
            res.append(op)
        except:
            if op == "+":
                res.append(res[-1] + res[-2])
            elif op == "D":
                res.append(res[-1]*2)
            elif op == "C":
                res.pop()
    return sum(res)

ops = ["5","2","C","D","+"]
print(calPoints(ops))
ops = ["5","-2","4","C","D","9","+","+"]
print(calPoints(ops))
ops = ["1","C"]
print(calPoints(ops))