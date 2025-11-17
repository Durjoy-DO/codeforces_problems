x=int(input())
count=0
for i in range(x):
    l=list(map(int,input().split()))
    if(l[1]-l[0]>=2):
        count=count+1

print(count)