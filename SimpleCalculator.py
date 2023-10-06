#solving the issue and added an exponent function which you can use

def add(a, z):
    return a + z

def subtract(a, z):
    return a - z

def multiply(a, z):
    return a * z

def divide(a, z):
    return a / z

def exponent(a, z):
    return a ** z 

print("Exponent Function added by Abhishek")

print("Select operation.")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Exponentiation")  

while True:
    choice = input("Enter choice(1/2/3/4/5): ")
    
    if choice in ('1', '2', '3', '4', '5'):
        numb1 = float(input("Enter first number: "))
        numb2 = float(input("Enter second number: "))
        
        if choice == '1':
            print(numb1, "+", numb2, "=", add(numb1, numb2))
        elif choice == '2':
            print(numb1, "-", numb2, "=", subtract(numb1, numb2))
        elif choice == '3':
            print(numb1, "*", numb2, "=", multiply(numb1, numb2))
        elif choice == '4':
            if numb2 == 0:
                print("Division by zero is not allowed.")
            else:
                print(numb1, "/", numb2, "=", divide(numb1, numb2))
        elif choice == '5':
            print(numb1, "**", numb2, "=", exponent(numb1, numb2))
        break
    else:
        print("Invalid Input")
