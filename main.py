print("Pragya Goyal - 25BCE10111")
print("------------------------------")
print(" SMART TASK PRIORITY SYSTEM")
print("------------------------------")
tasks=[]
n = int(input("Enter number of tasks: "))
for i in range(n):
    name = input("Task name: ")
    priority = input("Priority (High/Medium/Low): ")
    deadline = int(input("Days left: "))
    time_required = int(input("Time needed (hrs): "))

    task = {
        "name": name,
        "priority": priority,
        "deadline": deadline,
        "time": time_required
    }
    tasks.append(task)
priority_map = {
    "high": 3,
    "medium": 2,
    "low": 1
}
for task in tasks:
    priority_score = priority_map[task["priority"].lower()]
    urgency = max(0, 10 - task["deadline"])
    score = (priority_score * 5) + (urgency * 3) - task["time"]
    task["score"] = score
tasks.sort(key=lambda x: x["score"], reverse=True)
print("System Analysis:")
print("-------- RESULT --------")
count = 1
for task in tasks:
    print(str(count) + ". " + task['name'])
    print(f"   Score: {task['score']} | Priority: {task['priority']} | Deadline: {task['deadline']} days")
    if task["score"] > 30:
        print("   → High priority task")
    elif task["score"] > 16:
        print("   → Moderate priority task")
    else:
        print("   → Can be scheduled later")
    count += 1
