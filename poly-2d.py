def input_poly():
    poly = []
    while True:
        coeff = int(input("Enter Coefficient: "))
        deg = int(input("Enter Degree: "))
        poly.append([coeff, deg])
        done = input("Want to continue: ")
        if done == 'n':
            break
    return poly

def display_poly(poly):
    result = []
    n = len(poly)
    for i in range(n):
        result.append(f"{poly[i][0]}x^{poly[i][1]}")
    
    return " + ".join(result) if result else "0"

def evaluate_poly(poly, x):
    result = 0
    for coeff, deg in poly:
        result += coeff * (x ** deg)
    return result

def add_poly(p1, p2):
    result = []
    c1 = c2 = 0
    while(c1 < len(p1) and c2 < len(p2)):
        if(p1[c1][1] == p2[c2][1]):
            c = p1[c1][0] + p2[c2][0]
            result.append([c, p1[c1][1]])
            c1 += 1
            c2 += 1
        elif(p1[c1][1] > p2[c2][1]):
            result.append(p1[c1][0], p1[c1][1])
            c1 += 1
        else:
            result.append(p2[c2][0], p2[c2][1])
            c2 += 1
    
    while(c1 < len(p1)):
        result.append([p1[c1][0], p1[c1][1]])
        c1+=1
    while(c2 < len(c2)):
        result.append([p2[c2][0], p2[c2][1]])
        c1+=1
    return result

def multiply_poly(p1, p2):
    result = []

    for coeff1, deg1 in p1:
        for coeff2, deg2 in p2:
            new_c = coeff1 * coeff2
            new_d = deg1 + deg2
            found = False
            for i in range(len(result)):
                if result[i][1] == new_d:
                    result[i][0] += new_c
                    found = True
                    break
            if not found:
                result.append([new_c, new_d])
    result = [term for term in result if term[0] != 0]
    result.sort(key = lambda x: x[1], reverse=True)
    return result