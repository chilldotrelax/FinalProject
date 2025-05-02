import copy

line1 = input().split() #Row Column N
line2 = input().split() #Key Received
line3 = input().split() #Matrix

r = int(line1[0])
c = int(line1[1])
N = int(line1[2])


decryptMethod = []
for i in range(0, len(line2), 2):
    swapper = line2[i:i+2]
    decryptMethod.append(swapper)
print(decryptMethod)


matrix = []
for i in range(0, len(line3), int(c)): 
    swapper = line3[i:i+int(c)] 
    matrix.append(swapper)

count = 0
while True:
    if N == 1:
        for i in range(0,len(decryptMethod)): #Enables access to the element index within matrix decryptMethod.
            if i % 2 == 0 or i == 0: #For any even i, represents a row swap.
                copyMatrix = copy.deepcopy(matrix)
                matrix[int(decryptMethod[i][1])]= copyMatrix[int(decryptMethod[i][0])]
                matrix[int(decryptMethod[i][0])] = copyMatrix[int(decryptMethod[i][1])]
                copyMatrix2 = copy.deepcopy(matrix)
            elif i % 2 != 0: #For any odd im represents a column swap.
                for j in range(0, len(matrix)): #For column swap, access the specified element individual index.
                    matrix[j][int(decryptMethod[i][1])] = copyMatrix2[j][int(decryptMethod[i][0])]
                    matrix[j][int(decryptMethod[i][0])] = copyMatrix2[j][int(decryptMethod[i][1])]
        break
    elif N > 1 and count < N:
        for i in range(0,len(decryptMethod)): #Enables access to the element index within matrix decryptMethod.
            if i % 2 == 0 or i == 0: #For any even i, represents a row swap.
                copyMatrix = copy.deepcopy(matrix)
                matrix[int(decryptMethod[i][1])]= copyMatrix[int(decryptMethod[i][0])]
                matrix[int(decryptMethod[i][0])] = copyMatrix[int(decryptMethod[i][1])]
                copyMatrix2 = copy.deepcopy(matrix)
            elif i % 2 != 0: #For any odd im represents a column swap.
                for j in range(0, len(matrix)): #For column swap, access the specified element individual index.
                    matrix[j][int(decryptMethod[i][1])] = copyMatrix2[j][int(decryptMethod[i][0])]
                    matrix[j][int(decryptMethod[i][0])] = copyMatrix2[j][int(decryptMethod[i][1])]
        break