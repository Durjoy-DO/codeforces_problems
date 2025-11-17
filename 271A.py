x=int(input())
for i in range(x+1,10000):
    
    z=[i]
    number = z[0]
    digits = list(map(int, str(number)))
    if(len(digits)==len(set(digits))):
        print(number)
        exit()
    else:
        i=i+1

