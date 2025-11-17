n=int(input())
sum=0
z=[]
for i in range(n):
    x,y=map(int,input().split())
    sum=((sum+y)-x)
    z.insert(i,sum)
    
big=max(z)
print(big)