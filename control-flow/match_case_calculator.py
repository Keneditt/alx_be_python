num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")
result_message = ""
match operation:
    case "+":
        calculated_result = num1 + num2
        result_message = f"The result of {num1} + {num2} is {calculated_result}."
        print(f"The result is {calculated_result}.")
    case "-":
        calculated_result = num1 - num2
        result_message = f"The result is {calculated_result}."
        print(f"The result of {num1} - {num2} is {calculated_result}.")
    case "*":
        calculated_result = num1 * num2 
        print(f"The result of {num1} * {num2} is {calculated_result}.")
    case "/":
        if num2 != 0:
            calculated_result = num1 / num2
            result_message = f"The result is {calculated_result}." 
            print(f"The result is {calculated_result}.")
        else:
            result_message = "Cannot divide by zero."
    case _:
        result_message = "Error: Invalid operation chosen."
print(result_message)        