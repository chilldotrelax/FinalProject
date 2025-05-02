def matrixBuilder(coln,matrix_data):
    matrix = []
    for i in range(0, len(matrix_data), coln):
        builder = matrix_data[i:i+coln]
        matrix.append(builder)
    return matrix

def matrixSymmetricVerify(row, coln, matrixBuilt):
    score = 0
    if row != coln: matrixTransposer(row,coln,score, matrixBuilt)
    else:
        for i in range(0,row):
            if matrixBuilt[i] == [matrixBuilt[j][i] for j in range(0,row)]: 
                score += 1
                if score == (row - 1): matrixTransposer(row,coln,score, matrixBuilt)
                continue
            else: matrixTransposer(row,coln,score, matrixBuilt)

def matrixTransposer(row,coln,score,matrixBuilt):
    if score != (row - 1) or score == 0:
        newList = []
        if row == coln:
            for i in range(0,row):
                for j in range(0,coln):
                    newList.append(matrixBuilt[j][i])
            newListA = " ".join(newList)
            print(f'N {coln} {row}\n{newListA}')
        elif row > coln:
            for i in range(0,coln):
                for j in range(0,row):
                    newList.append(matrixBuilt[j][i])
            newListA = " ".join(newList)
            print(f'N {coln} {row}\n{newListA}')
    else:
        newList2 = []
        for i in range(row):
            newList2.append(matrixBuilt[i][i])
        newList3 = " ".join(newList2)
        print(f'S {row} {coln}\n{newList3}')


test_cases = int(input())
count = 0
while count < test_cases:
    row_and_coln = input().split()
    row = int(row_and_coln[0])
    coln = int(row_and_coln[1])

    matrix_data = input().split()

    matrixBuilt = matrixBuilder(coln,matrix_data)

    matrixSymmetricVerify(row, coln, matrixBuilt)
   
    count += 1