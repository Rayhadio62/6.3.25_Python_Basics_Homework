
print("Simple Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        choice = input("Choose operation (1-4): ")

        if choice == '1':
                result = num1 + num2
                print(f"{num1} + {num2} = {result}")
        elif choice == '2':
                result = num1 - num2
                print(f"{num1} - {num2} = {result}")
        elif choice == '3':
                result = num1 * num2
                print(f"{num1} * {num2} = {result}")
        elif choice == '4':
                while num2 == 0:
                        print("Error: Cannot divide by zero.")
                        try:
                                num2 = float(input("Please enter a non-zero number for the second value: "))
                        except ValueError:
                                print("Invalid input. Please enter a numeric value.")
                                continue
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")

        else:
            print("Invalid operation. Please select from 1 to 4.")
except ValueError:
        print("Invalid input. Please enter numeric values.")