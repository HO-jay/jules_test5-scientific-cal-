import math

class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y

    def power(self, x, y):
        return x ** y

    def sqrt(self, x):
        if x < 0:
            raise ValueError("Cannot take the square root of a negative number")
        return math.sqrt(x)

    def log(self, x, base=10):
        if x <= 0:
            raise ValueError("Cannot take the logarithm of a non-positive number")
        if base <= 0 or base == 1:
            raise ValueError("Logarithm base must be positive and not equal to 1")
        return math.log(x, base)

    def ln(self, x):
        if x <= 0:
            raise ValueError("Cannot take the natural logarithm of a non-positive number")
        return math.log(x)

    def sin(self, x):
        return math.sin(x)

    def cos(self, x):
        return math.cos(x)

    def tan(self, x):
        return math.tan(x)

if __name__ == "__main__":
    calc = Calculator()
    print("Simple CLI Calculator")
    print("Enter operation and numbers (e.g., 'add 5 3', 'sqrt 16', 'log 100 10').")
    print("Type 'quit' or 'exit' to end.")

    while True:
        try:
            user_input = input("> ").strip().lower()

            if user_input in ['quit', 'exit']:
                print("Exiting calculator.")
                break

            parts = user_input.split()
            if not parts:
                continue

            operation = parts[0]
            args = []
            try:
                args = [float(arg) for arg in parts[1:]]
            except ValueError:
                print("Error: All arguments must be numbers.")
                continue

            result = None
            if operation == 'add':
                if len(args) != 2:
                    print("Error: 'add' requires two numbers.")
                    continue
                result = calc.add(args[0], args[1])
            elif operation == 'subtract':
                if len(args) != 2:
                    print("Error: 'subtract' requires two numbers.")
                    continue
                result = calc.subtract(args[0], args[1])
            elif operation == 'multiply':
                if len(args) != 2:
                    print("Error: 'multiply' requires two numbers.")
                    continue
                result = calc.multiply(args[0], args[1])
            elif operation == 'divide':
                if len(args) != 2:
                    print("Error: 'divide' requires two numbers.")
                    continue
                result = calc.divide(args[0], args[1])
            elif operation == 'power':
                if len(args) != 2:
                    print("Error: 'power' requires two numbers (base exponent).")
                    continue
                result = calc.power(args[0], args[1])
            elif operation == 'sqrt':
                if len(args) != 1:
                    print("Error: 'sqrt' requires one number.")
                    continue
                result = calc.sqrt(args[0])
            elif operation == 'log':
                if len(args) == 1:
                    result = calc.log(args[0]) # Default base 10
                elif len(args) == 2:
                    result = calc.log(args[0], args[1]) # Custom base
                else:
                    print("Error: 'log' requires one number and an optional base.")
                    continue
            elif operation == 'ln':
                if len(args) != 1:
                    print("Error: 'ln' requires one number.")
                    continue
                result = calc.ln(args[0])
            elif operation == 'sin':
                if len(args) != 1:
                    print("Error: 'sin' requires one number (angle in radians).")
                    continue
                result = calc.sin(args[0])
            elif operation == 'cos':
                if len(args) != 1:
                    print("Error: 'cos' requires one number (angle in radians).")
                    continue
                result = calc.cos(args[0])
            elif operation == 'tan':
                if len(args) != 1:
                    print("Error: 'tan' requires one number (angle in radians).")
                    continue
                result = calc.tan(args[0])
            else:
                print(f"Error: Unknown operation '{operation}'.")
                print("Supported operations: add, subtract, multiply, divide, power, sqrt, log, ln, sin, cos, tan")
                continue

            print(f"Result: {result}")

        except ValueError as ve:
            print(f"Calculator Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
