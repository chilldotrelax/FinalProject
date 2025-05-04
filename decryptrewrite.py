'''
Andy Huang (ECE 160) Decrypter Rewrite
'''
rcn = input().split()
r = int(rcn[0])
c = int(rcn[1])
n = int(rcn[2])
decryptMethod = input().split()
data = input().split()

matrix = []
for i in range(0,len(data), c):
    a = data[i:i+c]
    matrix.append(a)

decrypt = []
for i in range(0, len(decryptMethod), 2):
    a = decryptMethod[i:i+2]
    decrypt.append(a)

while n > 0:
    for i in range(0,len(decrypt)):
        if i % 2 == 0: 
            matrix[int(decrypt[i][0])], matrix[int(decrypt[i][1])] = matrix[int(decrypt[i][1])],matrix[int(decrypt[i][0])]
        elif i % 2 != 0:
            for k in range(0,len(matrix)):
                matrix[k][int(decrypt[i][0])], matrix[k][int(decrypt[i][1])] = matrix[k][int(decrypt[i][1])],matrix[k][int(decrypt[i][0])]
    n += -1
        
for row in matrix:      
    print(' '.join(row))

