# Ask the user to enter the task
task = input("Enter your task: ")

# Ask for priority and convert it to lowercase
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound and convert to lowercase
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use match case to set the base reminder message based on priority
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Reminder: '{task}' is a low priority task"
    case _:
        reminder = f"Reminder: '{task}' has an unknown priority level"

# Use if statement to modify the reminder if time-bound
if time_bound == "yes":
    if priority in ["high", "medium"]:
        reminder += " that requires immediate attention today!"
    else:
        reminder += ". Consider completing it soon."
else:
    if priority == "low":
        reminder += ". Consider completing it when you have free time."
    else:
        reminder += "."

# Print the final customized reminder
print(reminder)
