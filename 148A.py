k=int(input())
l=int(input())
m=int(input())
n=int(input())
d=int(input())

s=set()
for i in range(1,d+1):
    if(i%k==0):
        s.add(i)
    elif(i%l==0):
        s.add(i)
    elif(i%m==0):
        s.add(i)
    elif(i%n==0):
        s.add(i)
    
print(len(s))


