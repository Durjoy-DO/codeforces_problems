
t = int(input().strip())
for _ in range(t):
    n = input().strip()
    
    ans = []
    L = len(n)
    for i, ch in enumerate(reversed(n)):  
        d = int(ch)
        if d != 0:
            ans.append(d * (10**i))
    print(len(ans), *ans)
