task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print("Reminder: '",task ,"' is a high priority task that requires immediate attention today!")
        elif time_bound == "no":
            print("Note: '", task, "' is a low priority task. Consider Completing it when you have free time.")
    case "medium":
        if time_bound == "yes":
            print("Reminder: '",task ,"' is a medium priority task that requires immediate attention today!")
        elif time_bound == "no":
            print("Note: '", task , "' is a low priority task. Consider Completing it when you have free time.")
    case "low":
        if time_bound == "yes":
            print("Reminder: '",task ,"' is a low priority task that requires immediate attention today!")
        elif time_bound == "no":
            print("Note: '", task, "' is a low priority task. Consider Completing it when you have free time.")