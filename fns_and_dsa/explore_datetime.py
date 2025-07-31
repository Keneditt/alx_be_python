from datetime import datetime, timedelta

def display_current_datetime():
    # Get current date and time
    current_date = datetime.now()
    # Format as "YYYY-MM-DD HH:MM:SS"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date(days):
    # Calculate future date
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    # Format as "YYYY-MM-DD"
    formatted_future = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future}")
    return future_date

def main():
    # Part 1: Display current datetime
    display_current_datetime()
    
    # Part 2: Calculate future date
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days)
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    main()