s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
s = list(s.replace(".","") .split())
ans = []
for w in s:
    ans.append(len(w))
print(ans)