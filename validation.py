from datetime import datetime
def validate_task_title(title):
   # title=""
    title = title.strip()

    if len(title) == 0:
        raise ValueError("Task title cannot be empty")
    return True    

def validate_task_description(description):
    description = description.strip()
    if len(description) == 0:
        raise ValueError("Task description cannot be empty")
    return True

def validate_due_date(due_date):
    due_date = due_date.strip()
    try:
        #Trying to parse the date in the format YYYY-MM-DD
         datetime.strptime(due_date, '%Y-%m-%d')
         return True
    except ValueError:
        raise ValueError ("Invalid date format. Please enter the data in the format YYYY-MM-DD")



