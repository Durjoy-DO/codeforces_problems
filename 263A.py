# Codeforces 263A - Beautiful Matrix

matrix = [[],[],[],[],[]]
for i in range(5):
    row = list(map(int, input().rstrip().split()))
    matrix[i]=row

location=[]
for i in range (5):
    for j in range (5):
        if matrix[i][j]==1:
            location=[i,j]



# Calculate Manhattan distance to center (3,3)
moves = abs(location[0] - 2) + abs(location[1] - 2)
print(moves)
