def ngramset(str,n):
    ans = set()
    for i in range(len(str)-n+1):
        ans.add(str[i:i+n])
    # ans = set([ str[i:i+n] for i in range(len(str)-n+1)])
    return ans

X = ngramset("paraparaparadise",2)
Y = ngramset("paragraph",2)
#和集合
print(X | Y)
#積集合
print(X & Y)
#差集合X\Y
print(X - Y)
#差集合Y\X
print(Y - X)

if "se" in X & Y:
    print("Yes")
else:
    print("No")