def ngram(str,n):
    ans = []
    for i in range(len(str)-n+1):
        ans.append(str[i:i+n])
    # ans = [ str[i:i+n] for i in range(len(str)-n+1)]
    return ans

s = "I am an NLPer"
print(ngram(s,1))
print(ngram(s,2))