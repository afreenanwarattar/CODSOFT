def display_menu():
    """show multiple options."""
    print("\n======================")
    print("     Task Manager     ")
    print("======================")
    print("1️⃣  Add New Tasks")
    print("2️⃣  View Task List")
    print("3️⃣  Mark Task as Completed")
    print("4️⃣  Exit")

def add_task(task_list):
    """ user can add as many task as they want."""
    try:
        N= int(input("\nHow many tasks would you like to add? "))
        for i in range(N):
            new_task = input(f"Enter task {i + 1}: ").strip()
            if new_task:
                task_list.append({"task": new_task, "status": "🕒 In Progress"})
                print("✅ Task successfully added!")
            else:
                print("⚠ Task cannot be empty. Please enter a valid task.")
    except ValueError:
        print("❌ Invalid input. Please enter a valid number.")

def view_tasks(task_list):
    """Displays all tasks with their current status."""
    print("\n📝 TASK LIST:\n")
    if not task_list:
        print("No tasks have been added yet.")
    else:
        for idx, task in enumerate(task_list, start=1):
            status = "✅ Completed" if task["status"] == "✅ Completed" else "🕒 In Progress"
            print(f"{idx}. {task['task']} - {status}")

def mark_task_completed(task_list):
    """User can mark completed task."""
    if not task_list:
        print("⚠ No tasks.")
        return
    try:
        index = int(input("Enter the number of the task you want to complete: ")) - 1

        if 0 <= index < len(task_list):
            task_list[index]["status"] = "✅ Completed" 
            print(f"✅ Task '{task_list[index]}' marked as completed.")
            
        else:
            print("⚠ Invalid task number. Please enter a valid task number.")

    except ValueError:
        print("⚠ Invalid input. Please enter a number.")
def main():
    task = []
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            add_task(task)
        elif choice == "2":
            view_tasks(task)
        elif choice == "3":
            mark_task_completed(task)
        elif choice == "4":
            print(" Exiting ")
            break
        else:
            print("⚠ Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

