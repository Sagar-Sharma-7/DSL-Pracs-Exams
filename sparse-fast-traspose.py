def getMatrix():
    m = int(input("Enter number of rows: "))
    n = int(input("Enter number of columns: "))
    matrix = []
    count = 0
    for i in range(m):
        for j in range(n):
            x = int(input(f"Enter element for a[{i+1}][{j+1}]"))
            if x != 0:
                matrix.append([i, j, x])
                count += 1
    
    return [[m, n, count]] + matrix

def simpleTrans(mat):
    rows, cols, non_zero = mat[0]
    transMat = [[cols, rows, non_zero]]
    trans_elements = []

    for i in range(1, non_zero + 1):
        r,c,v = mat[i]
        trans_elements.append([c,r,v])
    
    trans_elements.sort()
    transMat.extend(trans_elements)
    return transMat

def fastTranspose(mat):
    rows, cols, non_zero = mat[0]
    result = [[cols, rows, non_zero]] + [0] * non_zero
    print(result)
    rterm = [0] * cols

    for i in range(1, len(mat)):
        rterm[mat[i][1]] += 1
    print("rterm: ", rterm)

    rpos = [0] * (cols + 1)
    rpos[0] = 1
    for i in range(1, len(rpos)):
        rpos[i] = rpos[i-1] + rterm[i-1]
    print("\nrpos: ", rpos)

    for i in range(1, len(mat)):
        col = mat[i][1]
        index = rpos[col]
        result[index] = [col, mat[i][0], mat[i][2]]
        rpos[col] += 1
    return result

original_matrix = getMatrix()
original_matrix2 = original_matrix
print("Original Matrix:", original_matrix)

simple_transposed = simpleTrans(original_matrix)
print("Simple Transposed Matrix:", simple_transposed)

fast_transposed = fastTranspose(original_matrix2)
print("Fast Transposed Matrix:", fast_transposed)