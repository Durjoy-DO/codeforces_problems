k,n,w=map(int,input().split())
if(((k*w*(w+1))/2)>n):
     print(int(((k*w*(w+1))/2)-n))

else:
     print(0)