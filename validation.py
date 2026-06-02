from datetime import datetime
def validate_task_title(title):
   # title=""
    title = title.strip()

    if len(title) == 0:
        print ("Task title cannot be empty")
        return False
    return True    

def validate_task_description(description):
    description = description.strip()
    if len(description) == 0:
        print ("Task description cannot be empty")
        return False
    return True

def validate_due_date(due_date):
    due_date = due_date.strip()
    try:
        #Trying to parse the date in the format YYYY-MM-DD
         datetime.strptime(due_date, '%Y-%m-%d')
         return True
    except ValueError:
        print ("Invalid date format. Please enter the data in the format YYYY-MM-DD")
        return False


