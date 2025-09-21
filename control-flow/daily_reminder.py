task = input("Enter your task: ")

priority = input("Priority (high/medium/low): ")

time_bound = input("Is it time-bound? (yes/no): ")

reminder = ""

match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        
        print("Invalid priority. Please enter high, medium, or low.")
        exit()

if time_bound == "yes":
    
    if priority.lower() in ["high", "medium", "low"]:
        reminder += " that requires immediate attention today!"
else:
    if priority.lower() == "low":
        reminder += ". Consider completing it when you have free time."

print(reminder)
