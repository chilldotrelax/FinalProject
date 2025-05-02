'''
Andy Huang ECE 160 (Encrypter)

'''

#Import two important modules.
import random
import copy

line1 = input().split()
encryptdata = input().split() #Matrix you want to encrypt.

#Assign 
r = line1[0]
c = line1[1]
N = random.randrange(10)


#Creates some random numbers based on N (rows), should not exceed the number of columns to prevent out of range.
shuffler = []
if r == c:
    for i in range(N * 2):
        shuffler.append(random.randrange(0,int(c))) #Shouldnt exceed length of data.
else:
    for i in range(N * 2):
        shuffler.append(random.randrange(0,int(c) - 1))

swaps = []
for i in range(0, len(shuffler), 2): #Two cols max per N.
    swapper = shuffler[i:i+2]
    swaps.append(swapper)


#Converts encrypt data into matrix.
matrix = []
for i in range(0, len(encryptdata), int(c)): 
    swapper = encryptdata[i:i+int(c)]
    matrix.append(swapper)


copyMatrix = tuple(matrix)
count = 0


#Encrypts Matrix
while True:
    if N == 1:
        for k in range(0,N):
            if k % 2 == 0 or k == 0: #Swaps row, even
                copyMatrix = tuple(matrix)
                matrix[int(swaps[k][1])]= copyMatrix[int(swaps[k][0])]
                matrix[int(swaps[k][0])] = copyMatrix[int(swaps[k][1])]
                copyMatrix2 = copy.deepcopy(matrix)
            elif k % 2 != 0: #Swaps column, odd
                for i in range(0, len(matrix)):
                    matrix[i][int(swaps[k][1])] = copyMatrix2[i][int(swaps[k][0])]
                    matrix[i][int(swaps[k][0])] = copyMatrix2[i][int(swaps[k][1])]
        break
    elif N > 1 and count < N: #If N is more than 1 , repeat the process N - times.
        for k in range(0,N):
            if k % 2 == 0 or k == 0: #Swaps row, even
                copyMatrix = tuple(matrix)
                
                matrix[int(swaps[k][1])]= copyMatrix[int(swaps[k][0])]
                matrix[int(swaps[k][0])] = copyMatrix[int(swaps[k][1])]

                copyMatrix2 = copy.deepcopy(matrix)
            elif k % 2 != 0: #Swaps column, odd
                for i in range(0, len(matrix)):
                    matrix[i][int(swaps[k][1])] = copyMatrix2[i][int(swaps[k][0])]
                    matrix[i][int(swaps[k][0])] = copyMatrix2[i][int(swaps[k][1])]
        count += 1
        continue
    else: #If conditon 2 is false break and move on.
        break



print(f'{r} {c} {N}')

for i in range(len(swaps)):
    for j in range(2):
        print(f'{swaps[i][j]}',end=' ')

print()   

#Decompose matrix
for i in range(len(matrix)):
    for j in range(int(c)):
        print(f'{matrix[i][j]}',end=' ')




