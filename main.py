# Import functions from task_manager.task_utils package
from task_manager.task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress
# Define the main function
def main():
    tasks_List = []
    while True:
        print("Task Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            while True:
                title=input("Enter Task Title: ").strip()
                if validate_task_title(title):
                    break
            while True:        
                description = input("Enter Task Decsription: ")
                if validate_task_description(description):
                    break
            while True:     
                due_date = input("Enter Due Date (YYYY-MM-DD): ")
                if validate_due_date(due_date):
                    break
                add_task(title, description,due_date, tasks_List)

        elif choice == "2":
            view_pending_tasks(tasks_List)
            selection= input("Enter the index of the task to mark as complete: ")
            try:
                index = int(selection)
                mark_task_as_complete(index,tasks_List)
            except ValueError:
                print("Invalid input. Please enter a valid task index.")

        elif choice == "3":
            print("Pending Tasks:")
            view_pending_tasks(tasks_List)

        elif choice == "4":
            progress_percentage = calculate_progress(tasks_List)
            print(f"Progress: {progress_percentage:.2f}%")
        elif choice == "5":

            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
