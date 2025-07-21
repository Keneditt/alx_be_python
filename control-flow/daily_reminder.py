task_description = input("Enter your task: ")
while True:
    task_priority = input("Priority (high/medium/low): ").lower()
    if task_priority in ["high", "medium", "low"]:
        break
    else:
        print("Invalid priority. Please enter 'high', 'medium', or 'low'.")
while True:
    time_bound_input = input("Is this task time-bound? (yes/no): ").lower()
    if time_bound_input in ["yes", "no"]:
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
is_time_bound = (time_bound_input) == "yes"
reminder = ""
match task_priority:
    case "high":
        reminder = f"reminder: '{task_description}' is a high priority task."
    case "medium":
        reminder = f"reminder: '{task_description}' is a medium priority task."
    case "low":
        reminder = f"reminder: '{task_description}' is a low priority task."
    case _:
        reminder = f"reminder: '{task_description}' has an unknown priority task."
if is_time_bound:
    reminder += " that requires immediate attention today!"
else:
    reminder += "."
print(reminder)
     




          