
# calculator_console.py

import logging

# Setup logging
logging.basicConfig(filename='calculator_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def main():
    print("Simple Calculator")
    while True:
        try:
            print("\nOperations: +, -, *, / or 'exit'")
            op = input("Choose operation: ")
            if op == 'exit':
                break
            if op not in ['+', '-', '*', '/']:
                print("Invalid operation!")
                continue

            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if op == '+':
                result = add(a, b)
            elif op == '-':
                result = subtract(a, b)
            elif op == '*':
                result = multiply(a, b)
            elif op == '/':
                result = divide(a, b)

            print(f"Result: {result}")
            logging.info(f"{a} {op} {b} = {result}")

        except ValueError as e:
            print("Error:", e)
            logging.error(e)
        except Exception as e:
            print("Unexpected error:", e)
            logging.error("Unexpected error: " + str(e))

if __name__ == "__main__":
    main()
