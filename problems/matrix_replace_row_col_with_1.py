# in a given matrix of 0,1. If a location contains 1, replace row & col with 1.

matrix = [
    [0,1 ,0, 0],
    [0,0 ,0, 0],
    [0,0 ,1, 0],
    [0,0 ,0, 0],
]

def replace_col_row_with_one(matrix):
    rowset = set()
    colset = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                rowset.add(i)
                colset.add(j)
                print("found , ", i,j)
    
    print(rowset, colset)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i in rowset or j in colset:
                matrix[i][j] = 1
        print(matrix[i]) #  also print
            
replace_col_row_with_one(matrix)
