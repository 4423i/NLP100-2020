import random
with open('RandomStr.txt','w') as f:
    i = 10**6
    for _ in range(i):
        f.write(str(random.randrange(i)))
