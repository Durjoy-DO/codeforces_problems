x=int(input())
list=[]
for i in range(x):
    value=int(input())
    list.append(value)
count=1
for i in range(1,x):
    if(list[i-1]==list[i]):
        count=count
    elif(list[i-1]!=list[i]):
        count=count+1

print(count)

     