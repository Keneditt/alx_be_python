# main.py
from arithmetic_operations import perform_operation

def main():
    print("Arithmetic Operations")
    
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
        
        result = perform_operation(num1, num2, operation)
        
        if isinstance(result, str) and "Error" in result:
            print(f"Result: {result}")
        else:
            print(f"Result: {result:.1f}" if result.is_integer() else f"Result: {result}")
    
    except ValueError:
        print("Invalid input! Please enter valid numbers.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()