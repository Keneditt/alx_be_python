def main():
    # Prompt for task information
    task = input("Enter your task: ")
    
    # Get priority with validation
    while True:
        priority = input("Priority (high/medium/low): ").lower()
        if priority in ['high', 'medium', 'low']:
            break
        print("Invalid priority. Please enter high, medium, or low.")
    
    # Get time-bound status with validation
    while True:
        time_bound = input("Is it time-bound? (yes/no): ").lower()
        if time_bound in ['yes', 'no']:
            break
        print("Invalid response. Please enter yes or no.")
    
    # Generate reminder using match-case and if statements
    match priority:
        case 'high':
            message = f"Reminder: '{task}' is a high priority task"
            if time_bound == 'yes':
                message += " that requires immediate attention today!"
            else:
                message += ". Please address this soon."
        
        case 'medium':
            message = f"Note: '{task}' is a medium priority task"
            if time_bound == 'yes':
                message += " that should be completed by the end of the day."
            else:
                message += ". Try to complete it this week."
        
        case 'low':
            message = f"Note: '{task}' is a low priority task"
            if time_bound == 'yes':
                message += " with a specific deadline. Schedule time for it."
            else:
                message += ". Consider completing it when you have free time."
    
    # Print the customized reminder
    print("\n" + message)

if __name__ == "__main__":
    main()
     


          