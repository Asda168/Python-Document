import json
import os

FILE = "tasks.json"


def load_tasks():
    if not os.path.exists(FILE):
        return []

    with open(FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("Task added!")


def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("⚠️ No tasks found.")
        return

    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")


def delete_task(index):
    tasks = load_tasks()

    if 0 < index <= len(tasks):
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"🗑️ Deleted: {removed}")
    else:
        print("❌ Invalid index")


def main():
    while True:
        print("\n=== TO-DO LIST ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            task = input("Enter task: ").strip()
            if task:
                add_task(task)
            else:
                print("❌ Task cannot be empty")

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            try:
                index = int(input("Enter task number: "))
                delete_task(index)
            except ValueError:
                print("❌ Please enter a valid number")

        elif choice == "4":
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice")


if __name__ == "__main__":
    main()