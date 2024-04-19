class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
        else:
            print("Invalid task index.")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks.")
        else:
            for i, task in enumerate(self.tasks):
                status = "✔" if task["completed"] else "❌"
                print(f"{i + 1}. [{status}] {task['task']}")

def main():
    todo_list = ToDoList()
    while True:
        print("\n1. Add Task")
        print("2. Mark Task as Completed")
        print("3. Show Tasks")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == "2":
            index = int(input("Enter task index to mark as completed: ")) - 1
            todo_list.mark_task_completed(index)
        elif choice == "3":
            todo_list.show_tasks()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
