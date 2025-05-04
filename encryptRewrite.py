import random

rc = input().split()
data = input().split()
r = int(rc[0])
c = int(rc[1])
n = 1
ncopy1 = n * 4
ncopy = n
ncopy2 = n

shuffler = []
while (ncopy1) > 0:
    if r > c: 
        shuffler.append(random.randint(0,(c-1)))
        ncopy1 += -1
    else:
        shuffler.append(random.randint(0,(r-1)))
        ncopy1 += -1

encrypt = []
for i in range(0, len(shuffler), 2):
    swapper = shuffler[i:i+2]
    encrypt.append(swapper)

matrix = []
for i in range(0, len(data), int(c)): 
    swapper = data[i:i+int(c)]
    matrix.append(swapper)

while ncopy > 0:
    for i in range(0,len(encrypt)):
        if i % 2 == 0: 
            matrix[int(encrypt[i][0])], matrix[int(encrypt[i][1])] = matrix[int(encrypt[i][1])],matrix[int(encrypt[i][0])]
        elif i % 2 != 0:
            for k in range(0,len(matrix)):
                matrix[k][int(encrypt[i][0])], matrix[k][int(encrypt[i][1])] = matrix[k][int(encrypt[i][1])],matrix[k][int(encrypt[i][0])]
    ncopy += -1


print(f'{r} {c} {ncopy2}')


for i in range(len(encrypt)):
    for j in range(2):
        print(f'{encrypt[i][j]}',end=' ')

print()   

for i in range(len(matrix)):
    for j in range(int(c)):
        print(f'{matrix[i][j]}',end=' ')
