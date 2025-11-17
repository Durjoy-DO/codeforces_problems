x=int(input())
s=str(input())
count=0
x=list(s)
for i in range(len(x)-1):
    if(x[i]==x[i+1]):
        count=count+1
        i=i+1
    else:
        i=i+1
print(count)
