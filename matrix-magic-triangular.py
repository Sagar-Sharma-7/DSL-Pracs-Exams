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

def is_upper_triangular(matrix):
    for i in range(len(matrix)):
        for j in range(i):
            if matrix[i][j] != 0:
                return False
    return True

def is_magic_square(matrix):
    n = len(matrix)
    common_sum = sum(matrix[0])
    for row in matrix:
        if sum(row) != common_sum:
            return False
    for col in range(n):
        col_sum = 0
        for row in range(n):
            col_sum += matrix[row][col]
        if col_sum != common_sum:
            return False
    
    first_diagonal_sum = 0
    for i in range(n):
        first_diagonal_sum += matrix[i][i]
    if first_diagonal_sum != common_sum:
        return False

    second_diagonal_sum = 0
    for i in range(n):
        second_diagonal_sum += matrix[i][n - i - 1]
    if second_diagonal_sum != common_sum:
        return False
    
    return True

def main():
    matrix1 = [
        [1, 2],
        [3, 4]
    ]
    matrix2 = [
        [5, 6],
        [7, 8]
    ]
    matrix3 = [
        [2, 3, 4],
        [0, 5, 6],
        [0, 0, 7]
    ]
    magic_matrix = [
        [8, 1, 6],
        [3, 5, 7],
        [4, 9, 2]
    ]

    print("Addition of matrices:")
    result_add = add_matrices(matrix1, matrix2)
    for row in result_add:
        print(row)

    print("\nMultiplication of matrices:")
    result_mul = multiply_matrices(matrix1, matrix2)
    for row in result_mul:
        print(row)

    print("\nIs the matrix upper triangular?")
    print(is_upper_triangular(matrix3))

    print("\nIs the matrix a magic square?")
    print(is_magic_square(magic_matrix))

# Execute the program
main()