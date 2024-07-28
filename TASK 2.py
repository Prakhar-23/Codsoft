# Function to perform addition
def add(a, b):
    return a + b

# Function to perform subtraction
def subtract(a, b):
    return a - b

# Function to perform multiplication
def multiply(a, b):
    return a * b

# Function to perform division
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."

# Main function to run the calculator
def calculator():
    print("(((Simple Calculator)))")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    # Get the user's choice of operation
    choice = input("Enter choice (1/2/3/4): ")

    # Validate the choice
    if choice in ['1', '2', '3', '4']:
        try:
            # Get the numbers from the user
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            # Perform the chosen operation
            if choice == '1':
                result = add(num1, num2)
            elif choice == '2':
                result = subtract(num1, num2)
            elif choice == '3':
                result = multiply(num1, num2)
            elif choice == '4':
                result = divide(num1, num2)

            # Display the result
            print("Result:", result)
        except ValueError:
            print("Error: Invalid input. Please enter numeric values.")
    else:
        print("Error: Invalid choice. Please select a valid operation.")

# Run the calculator
if __name__ == "__main__":
    calculator()
