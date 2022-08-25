a = [1,2,3]
b = a.copy()
a[0] = 123
print(b)
print(a)
a[0] = b[2]
print(a,b)