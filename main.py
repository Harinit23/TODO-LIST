class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

    def view_list(self):
        return self.tasks

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index] += " (Completed)"
        else:
            print("Invalid task index.")

todo_list = TodoList()

while True:
    print("\nTo-Do List:")
    tasks = todo_list.view_list()
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

    print("\nOptions:")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. View the to-do list")
    print("4. Mark a task as completed")
    print("5. Quit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        task = input("Enter the task to add: ")
        todo_list.add_task(task)
        print(f"Task '{task}' added to the to-do list.")
    elif choice == '2':
        task = input("Enter the task to remove: ")
        if task in tasks:
            todo_list.remove_task(task)
            print(f"Task '{task}' removed from the to-do list.")
        else:
            print(f"Task '{task}' not found in the to-do list.")
    elif choice == '3':
        print("To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    elif choice == '4':
        index = int(input("Enter the index of the task to mark as completed: ")) - 1
        todo_list.complete_task(index)
        print("Task marked as completed!")
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")




