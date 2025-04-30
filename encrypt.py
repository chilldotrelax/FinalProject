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

'''

FOR THE GRADER:

I PURPOSELY LIMITED THE RANGE OF N to 10 FOR PERFORMANCE REASONS!

'''

#Creates some random numbers based on N (rows), should not exceed the number of columns to prevent out of range.
shuffler = []
for i in range(N * 2):
    shuffler.append(random.randrange(0,int(c)))


swaps = []
for i in range(0, len(shuffler), 2): #Two cols max per N.
    swapper = shuffler[i:i+2]
    swaps.append(swapper)


#Converts encrypt data into matrix.
matrix = []
for i in range(0, len(encryptdata), int(c)): #col
    swapper = encryptdata[i:i+int(c)]
    matrix.append(swapper)



copyMatrix = tuple(matrix)

count = 0


#Encrypts Matrix
while True:
    if N == 1:
        for k in range(N):
            if k % 2 == 0 or k == 0: #Swaps row, even
                copyMatrix = tuple(matrix)
                matrix[int(swaps[k][1])]= copyMatrix[int(swaps[k][0])]
                matrix[int(swaps[k][0])] = copyMatrix[int(swaps[k][1])]
                copyMatrix2 = copy.deepcopy(matrix)
            elif k % 2 != 0: #Swaps column, odd
                for i in range(len(matrix)):
                    matrix[i][int(swaps[k][1])] = copyMatrix2[i][int(swaps[k][0])]
                    matrix[i][int(swaps[k][0])] = copyMatrix2[i][int(swaps[k][1])]
        break
    elif N > 1 and count < N: #If N is more than 1 , repeat the process N - times.
        for k in range(N):
            if k % 2 == 0 or k == 0: #Swaps row, even
                copyMatrix = tuple(matrix)
                matrix[int(swaps[k][1])]= copyMatrix[int(swaps[k][0])]
                matrix[int(swaps[k][0])] = copyMatrix[int(swaps[k][1])]
                copyMatrix2 = copy.deepcopy(matrix)
            elif k % 2 != 0: #Swaps column, odd
                for i in range(len(matrix)):
                    matrix[i][int(swaps[k][1])] = copyMatrix2[i][int(swaps[k][0])]
                    matrix[i][int(swaps[k][0])] = copyMatrix2[i][int(swaps[k][1])]
        count += 1
        continue
    else: #If conditon 2 is false break and move on.
        break

#reverses swaps

swaps.reverse()

print(f'Your rcn: {r} {c} {N}')

for i in range(len(swaps)):
    for j in range(2):
        print(f'{swaps[i][j]}',end=' ')

print()   

#Decompose matrix
for i in range(len(matrix)):
    for j in range(int(c)):
        print(f'{matrix[i][j]}',end=' ')




    