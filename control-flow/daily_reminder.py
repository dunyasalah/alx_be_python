task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()


print(f"Reminder: You have a task '{task}' with {priority} priority.")


if time_bound == "yes":
    if priority in ["high", "medium"]:
        print("This task requires immediate attention today!")
    else:
        print("This task should be done soon.")
else:
    if priority == "low":
        print("You can complete this task when you have free time.")
    else:
        print("Keep this task in mind.")
