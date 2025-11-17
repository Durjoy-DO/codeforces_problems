n=int(input())
sum=0
arr = list(map(int, input().split()))

for i in range(n):
    sum=sum+(arr[i])


if(sum==0):
    print("EASY")
else:
    print("HARD")
