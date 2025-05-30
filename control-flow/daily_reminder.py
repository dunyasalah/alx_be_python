task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

if time_bound == "yes":
    if priority in ["high", "medium"]:
        time_msg = " that requires immediate attention today!"
    else:
        time_msg = ". Consider completing it soon."
else:
    if priority == "low":
        time_msg = ". Consider completing it when you have free time."
    else:
        time_msg = "."

match priority:
    case "high":
        print(f"Reminder: '{task}' is a high priority task{time_msg}")
    case "medium":
        print(f"Reminder: '{task}' is a medium priority task{time_msg}")
    case "low":
        print(f"Note: '{task}' is a low priority task{time_msg}")
    case _:
        print(f"Reminder: '{task}' has an unknown priority level{time_msg}")
