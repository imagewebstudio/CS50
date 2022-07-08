x = [[1,2,3],[4,5,6],[7,8,9]]
n = len(x)
for i in range(n):
    for j in range(n):
        if i != n-1 and j > 0:    
            x[i][j], x[j][i] = x[j][i], x[i][j]

print(x)

for i in range(n):
    x[i].reverse()
print(x)
