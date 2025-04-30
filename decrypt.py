'''
Andy Huang ECE 160 (Decrypter)

'''

#Import important module.
import copy

line1 = input().split() #Row Column N
line2 = input().split() #Key Received
line3 = input().split() #Matrix

#row, col, N 
r = int(line1[0])
c = int(line1[1])
N = int(line1[2])


#Convert new inputs to accessible matrix.
line2Matrix = []
for i in range(0, len(line2), 2): #Two cols max.
    swapper = line2[i:i+2]
    line2Matrix.append(swapper)

#Reverses line2Matrix => fit encrypter.

line2Matrix.reverse()

matrix = []

#Assign a matrix to data, row first column second
for i in range(0, len(line3), int(c)): #This determines the column length (step = c or column length)
    swapper = line3[i:i+int(c)] #Performs a list slice from line3 at some point of iteration at i to i after c.
    matrix.append(swapper)


#immutable copy
copyMatrix = tuple(matrix)
#Unscramble matrix using line2.
#every n is one row and one column 
count = 0

#I tweaked out writing this 
while True:
    if N == 1:
        for k in range(N):
            if k % 2 == 0 or k == 0: #Swaps row, even
                copyMatrix = tuple(matrix)
                matrix[int(line2Matrix[k][1])]= copyMatrix[int(line2Matrix[k][0])]
                matrix[int(line2Matrix[k][0])] = copyMatrix[int(line2Matrix[k][1])]
                copyMatrix2 = copy.deepcopy(matrix)
            elif k % 2 != 0: #Swaps column, odd
                for i in range(len(matrix)):
                    matrix[i][int(line2Matrix[k][1])] = copyMatrix2[i][int(line2Matrix[k][0])]
                    matrix[i][int(line2Matrix[k][0])] = copyMatrix2[i][int(line2Matrix[k][1])]
        break
    elif N > 1 and count < N: #If N is more than 1 , repeat the process N - times.
        for k in range(N):
            if k % 2 == 0 or k == 0: #Swaps row, even
                copyMatrix = tuple(matrix)
                matrix[int(line2Matrix[k][1])]= copyMatrix[int(line2Matrix[k][0])]
                matrix[int(line2Matrix[k][0])] = copyMatrix[int(line2Matrix[k][1])]
                copyMatrix2 = copy.deepcopy(matrix)
            elif k % 2 != 0: #Swaps column, odd
                for i in range(len(matrix)):
                    matrix[i][int(line2Matrix[k][1])] = copyMatrix2[i][int(line2Matrix[k][0])]
                    matrix[i][int(line2Matrix[k][0])] = copyMatrix2[i][int(line2Matrix[k][1])]
        count += 1
        continue
    else: #If conditon 2 is false break and move on.
        break

#Prints final matrix.
for g in range(r):
    for h in range(c):
        print(matrix[g][h],end=" ")
    print()