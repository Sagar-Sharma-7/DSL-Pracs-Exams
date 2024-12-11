def getmatrix():
    m = int(input("Enter number of rows: "))
    n = int(input("Enter number of cols: "))
    count = 0
    matrix = []
    for i in range(m):
        for j in range(n):
            x = int(input(f"Enter value for matrix[{i + 1}][{j + 1}]"))
            if(x != 0):
                matrix.append([i, j, x])
                count += 1
    return [[m, n, count]] + matrix

def simpleTrans(mat):
    rows, cols, non_zero = mat[0]
    transMat = [[cols, rows, non_zero]]
    trans_element = []
    for i in range(1, len(mat)):
        r,c,v = mat[i]
        trans_element.append([c,r,v])
    
    trans_element.sort()
    transMat.extend(trans_element)
    return transMat

def addmatrix(m1, m2):
    if(m1[0][0] == m2[0][0] and m1[0][1] == m2[0][1]):
        m = m1[0][0]
        n = m1[0][1]
        c1 = c2 = 1
        result = [[m, n, 0]]
        count = 0
        while(c1 < len(m1) and c2 < len(m2)):
            if(m1[c1][0] == m2[c2][0] and m1[c1][1] == m2[c2][1]):
                result.append([m1[c1][0], m1[c1][1], m1[c1][2] + m2[c2][2]])
                c1 += 1
                c2 += 1
                count += 1
            elif((m1[c1][0] == m2[c2][0] and m1[c1][1] < m2[c1][1]) or m1[c1][0] < m2[c2][0]):
                result.append([m1[c1][0], m1[c1][1], m1[c1][2]])
                c1+=1
                count += 1
            else:
                result.append([m2[c2][0], m2[c2][1], m2[c2][2]])
                c2 += 1
                count += 1
        
        while c1 < len(m1):
            result.append([m1[c1][0], m1[c1][1], m1[c1][2]])
            c1+=1
            count += 1
        while c1 < len(m2):
            result.append([m2][c2][0], m2[c2][1], m2[c2][2])
            c2 += 1
            count += 1

        result[0][2] = count
        return(result)
    else:
        print("Matrices can't be added")

m1 = getmatrix()
m2 = getmatrix()
print(addmatrix(m1, m2))
