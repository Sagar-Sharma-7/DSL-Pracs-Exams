def getMatrix():
    m = int(input("Enter number of rows: "))
    n = int(input("Enter number of columns:"))
    matrix = list()
    for i in range(m):
        x = []
        for j in range(n):
            x.append(int(input("Enter element for a[%d][%d]: "%(i+1,j+1))));
        matrix.append(x)

    return matrix


def add_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

def multiply_matrices(matrix1, matrix2):
    rows_matrix1 = len(matrix1)
    cols_matrix1 = len(matrix1[0])
    rows_matrix2 = len(matrix2)
    cols_matrix2 = len(matrix2[0])

    result = []
    for i in range(rows_matrix1):
        row = [0] * cols_matrix2
        result.append(row)

    for i in range(rows_matrix1):
        for j in range(cols_matrix2):
            for k in range(cols_matrix1):
                result[i][j] += matrix1[i][k] + matrix2[k][j]
    return result

def get_transpose(matrix):
    result = []
    for i in range(len(matrix[0])):
        new_row = []
        for j in range(len(matrix)):
            new_row.append(matrix[j][i])
        result.append(new_row)
    return result

def saddle(matrix):
    saddle_point = []
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        row_min = min(matrix[i])
        min_col_indices = [j for j in range(cols) if matrix[i][j] == row_min]

        for col_i in min_col_indices:
            is_saddle = True
            for k in range(rows):
                if matrix[k][col_i] > row_min:
                    is_saddle = False
                    break
            if is_saddle:
                saddle_point.append((i + 1, col_i + 1))
     
    return saddle_point
