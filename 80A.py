n,m=map(int,input().split())
p=0
for i in range(n+1,50):
    count=0
    for j in range(1,i+1):
       
        if(i%j==0):
            count=count+1
        else:
            count=count
    if(count==2):
        p=int(i)
        break
        
if(m==p):
    print("YES")

else:
    print("NO")
        