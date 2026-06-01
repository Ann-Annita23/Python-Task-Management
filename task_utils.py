from datetime import datetime
# Import validation functions
from task_manager.validation import validate_task_title, validate_task_description, validate_due_date
# Define tasks list
tasks_List = []
# Implement add_task function
def add_task(title, description, due_date, tasks_List):
    #Double checking the validation of the inputs
     if not validate_task_title(title) or not validate_task_description(description) or not validate_due_date(due_date):
        return False
     task={
       "title": title,
       "description": description,
       "due_date": due_date,
       "completed":False
        }
     tasks_List.append(task)
     print("Task added successfully!")
     return True

# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks_List):
     if index<0 or index>=len(tasks_List):
        print("Invalid task index")
        return False
     tasks_List[index]["completed"]=True
     print("Task marked as complete!")
     return True

# Implement view_pending_tasks function
def view_pending_tasks(tasks_List):
    #Enumarate is a structure each tuple is formatted in/ for
    for index, task in enumerate(tasks_List):
        if not task["completed"]:
            print(f"{index}. {task['title']} - Due: {task['due_date']}")


# Implement calculate_progress function
def calculate_progress(tasks_List):
    length = len(tasks_List)
    if length == 0:
        return 0
    completed_count = 0
    for task in tasks_List:
        if task["completed"]:
            completed_count += 1
    progress = (completed_count/length)*100    
    return progress           