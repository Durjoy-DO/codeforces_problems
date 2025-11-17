x=str(input())
parts = x.split("+")     # ['1', '2', '3']
result = "".join(parts)
p=sorted(result)
res="+".join(str(p))
print(res)

   