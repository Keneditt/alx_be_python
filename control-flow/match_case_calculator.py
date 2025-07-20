num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose an operation (+, -, *, /): ")
result_message = ""
match operation:
    case "+":
        calculated_result = num1 + num2
        result_message = f"The result of {num1} + {num2} is {calculated_result}."
    case "-":
        calculated_result = num1 - num2
        result_message = f"The result of {num1} - {num2} is {calculated_result}."
    case "*":
        calculated_result = num1 * num2 
    case "/":
        if num2 != 0:
            calculated_result = num1 / num2
            result_message = f"The result of {num1} / {num2} is {calculated_result}."
        else:
            result_message = "cannot divide by zero."
    case _:
        result_message = "Error: Invalid operation chosen."
print(result_message)        