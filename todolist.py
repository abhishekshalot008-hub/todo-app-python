import json

try:
    with open("tasks.json", "r") as f:
        tasks = json.load(f)
except FileNotFoundError:
    tasks = []

def save_tasks():
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)

while True:
    print("\n--- TO-DO APP ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Complete")
    print("4. Delete Task")
    print("5. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        task_text = input("Enter new task: ")
        tasks.append({"task": task_text, "done": False})
        save_tasks()
        print("Task added!")
    
    elif choice == "2":
        print("\nYour Tasks:")
        for index, t in enumerate(tasks):
            status = "✓" if t["done"] else "✗"
            print(index + 1, "-", t["task"], "[", status, "]")
    
    elif choice == "3":
        print("\nYour Tasks:")
        for index, t in enumerate(tasks):
            status = "✓" if t["done"] else "✗"
            print(index + 1, "-", t["task"], "[", status, "]")
        task_number = int(input("Enter task number to mark complete: "))
        tasks[task_number - 1]["done"] = True
        save_tasks()
        print("Task marked complete!")
    
    elif choice == "4":
        print("\nYour Tasks:")
        for index, t in enumerate(tasks):
            status = "✓" if t["done"] else "✗"
            print(index + 1, "-", t["task"], "[", status, "]")
        task_number = int(input("Enter task number to delete: "))
        tasks.pop(task_number - 1)
        save_tasks()
        print("Task deleted!")
    
    elif choice == "5":
        print("Goodbye!")
        break
    
    else:
        print("Invalid option, try again")