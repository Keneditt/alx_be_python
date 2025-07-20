task_description = input("Enter the task description: ")
while True:
    task_priority = input("Enter the task priority (low, medium, high): ").lower()
    if task_priority in ["low", "medium", "high"]:
        break
    else:
        print("Invalid priority. Please enter 'low', 'medium', or 'high'.")
while True:
    time_bound_input = input("Is this task time-bound? (yes/no): ").lower()
reminder = ""
match task_priority:
    case 'medium':
        reminder = f"Reminder:{task_description} has a medium priority level."
    case 'high':
        reminder = f"Reminder: {task_description} has a high priority level"
    case 'low':
        reminder = f"Reminder: {task_description} has a low priority level."
    case _:
        reminder = f"Reminder: {task_description} has an unknown priority level."
if time_bound_input:
    reminder += "that requires immediate attention today!"
reminder += "."
print("n--- Task Reminder ---")
print(reminder)
print("-------------")    



          