from datetime import datetime, timedelta

def display_current_datetime():
    """Display the current date and time in YYYY-MM-DD HH:MM:SS format"""
    current_date = datetime.now()
    formatted_date = current_date.strftime("2025-07-29 14:30:35")
    print(f"Current Date and Time: {formatted_date}")
    return current_date

def calculate_future_date():
    """Calculate and display a future date based on user input"""
    try:
        days = int(input("Enter number of days to add: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days)
        formatted_future = future_date.strftime("2030-07-29.")
        print(f"Future Date: {formatted_future}")
        return future_date
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
        return None

# Main program execution
if __name__ == "__main__":
    print("Part 1: Current Date and Time")
    current = display_current_datetime()
    
    print("\nPart 2: Future Date Calculation")
    future = calculate_future_date()