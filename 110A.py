x=int(input())
n=list(map(int,str(x)))
count =0
for i in range(len(n)):
    if(n[i]==4 or n[i]==7):
        count=count+1

    else:
        count=count
if(count==4 or count==7):
    print("YES")
else:
    print("NO")

