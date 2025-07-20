while True:
    try:
        pattern_size = int(input("Enter the size of the pattern: "))
        if pattern_size > 0:
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a whole number.")

current_row = 0
while current_row < pattern_size:
    current_column = 0
    while current_column < pattern_size:
        print("*", end="")
        current_column += 1
    print()  # Move to the next line after finishing a row
    current_row += 1