def average(salary: list) -> float:
    return ( sum(salary) - min(salary) - max(salary))  / ( len(salary) - 2 )

print(average([4000,3000,1000,2000]))