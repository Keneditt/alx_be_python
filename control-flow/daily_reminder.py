def perform_operation(num1, num2, operation):
    """
    Performs basic arithmetic operations on two numbers.
    
    Args:
        num1: First operand
        num2: Second operand
        operation: Type of operation ('add', 'subtract', 'multiply', 'divide')
        
    Returns:
        Result of the operation or error message for division by zero
    """
    operation = operation.lower()  # Normalize input
    
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        raise ValueError("Invalid operation. Supported operations are: 'add', 'subtract', 'multiply', 'divide'")

     


          