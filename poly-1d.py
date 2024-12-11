def input_polynomial():
    degree = int(input("Enter the degree of polynomial: "))
    coeffs = []
    for i in range(degree, -1, -1):
        coeff = int(input(f"Enter the coefficient of x^{i}: "))
        coeffs.append(coeff)
    return coeffs

def output_polynomial(coeffs):
    terms = []
    degree = len(coeffs) - 1
    for i in range(len(coeffs)):
        power = degree - i
        if coeffs[i] != 0:
            if power == 0:
                terms.append(f"{coeffs[i]}")
            elif power == 1:
                terms.append(f"{coeffs[i]}x")
            else:
                terms.append(f"{coeffs[i]}x^{power}")
    return " + ".join(terms) if terms else "0"

def evaluate_polynomial(coeffs, x):
    result = 0
    degree = len(coeffs) - 1
    for i in coeffs:
        result += i*(x**(degree - i))
    return result

def add_polynomial(poly1, poly2):
    p1 = poly1[:]
    p2 = poly2[:]
    result = []
    diff = len(p1) - len(p2)
    if diff > 0:
        p2 = [0] * diff + poly2
    elif diff < 0:
        p1 = [0] * (-diff) + poly1
    
    for i in range(len(p1)):
        result.append(p1[i] + p2[i])
    
    while len(result) > 1 and result[0] == 0:
        result.pop(0)
    return result

def multiply_polynomials(poly1, poly2):
    degree1 = len(poly1) - 1
    degree2 = len(poly2) - 1
    result = [0] * (degree1 + degree2 + 1)

    for i in range(len(poly1)):
        for j in range(len(poly2)):
            result[i+j] += poly1[i] * poly2[j]
    return result

def main():
    print("Polynomial Operations:")
    print("1. Input and Output Polynomial")
    print("2. Evaluate Polynomial")
    print("3. Add Two Polynomials")
    print("4. Multiply Two Polynomials")
    print("5. Exit")

    while True:
        choice = int(input('\nEnter your choice: '))

        if choice == 1:
           poly = input_polynomial()
           print("Polynomial: ", output_polynomial(poly))
        elif choice == 2:
            poly = input_polynomial()
            x = int(input("Enter the value of x: "))
            print("Result: ", evaluate_polynomial(poly, x))
        elif choice == 3:
            print("Input first polynomial:")
            poly1 = input_polynomial()
            print("Input second polynomial:")
            poly2 = input_polynomial()
            result = add_polynomial(poly1, poly2)
            print("Resultant Polynomial: ", output_polynomial(result))
        elif choice == 4:
            print("Input first polynomial:")
            poly1 = input_polynomial()
            print("Input second polynomial:")
            poly2 = input_polynomial()
            result = multiply_polynomials(poly1, poly2)
            print("Resultant Polynomial: ", output_polynomial(result))
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid, trg again")

main()