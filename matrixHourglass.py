'''

Andy Huang (ECE 160: Hourglassr)

'''

def hourGlassr(matrix):
    maxSum = 0
    for i in range(0,len(matrix) - 2):
        for j in range(0,len(matrix[0]) - 2):
            valuesAdd = (matrix[i][j] + matrix[i][j + 1] + matrix[i][j + 2]) + (matrix[i + 1][j + 1]) + (matrix[i + 2][j] + matrix[i + 2][j + 1] + matrix[i + 2][j + 2])
            if valuesAdd > maxSum: maxSum = valuesAdd
    return maxSum
    
if __name__ == "__main__":
    matrix = []
    n = int(input())
    while n > 0:
        matrixData = input().split()
        for i in range(0,len(matrixData),len(matrixData)):
            a = matrixData[i:i+len(matrixData)]
            matrix.append([int(i) for i in a])
        n += -1
    
    print(hourGlassr(matrix))