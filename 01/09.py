import random 
def randomselect(s):
    ans = ""
    index = random.sample(range(len(s)), k = len(s))
    for i in index:
        ans += s[i]
    return ans

s = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
s = list(s.split(" "))
for i in range(len(s)):
    w = s[i]
    if len(w) <= 4:
        continue
    else:
        l,r = w[0],w[-1]
        ww = list(w[1:-2])
        s[i] = l + "".join(randomselect(ww)) + r

print(*s)