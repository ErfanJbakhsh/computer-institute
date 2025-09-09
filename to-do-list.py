import csv 

class Task():
    def __init__(self, name, description, priority):
        self.name = name
        self.description = description
        self.priority = priority
    def __str__(self):
        return f'task name is: {self.name} \ndescription: {self.description} \npriority: {self.priority}'
            
class ToDoList():
    def __init__(self):
        self.all_tasks = []
    def add_task(self, task: Task):
        for t in self.all_tasks:
            if t.name == task.name:
                print(f'{task.name} already exist!')
                return
        self.all_tasks.append(task)
        print(f'{task.name} was successfully added to list')
    def remove_task(self, name):
        for t in self.all_tasks: 
            if name == t.name:
                self.all_tasks.remove(t)
                print(f'{name} was successfully removed')
                continue
            print(f'{name} does not exist!')   
    def show_list(self):
        if len(self.all_tasks) == 0:
            print('your list is empty!')
        else:
            for task in self.all_tasks:
                print(task)
    def save_to_csv(self):
        with open(self.filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["name", "description", "priority"]) 
            for task in self.all_tasks:
                writer.writerow([task.name, task.description, task.priority])

    def load_from_csv(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    task = Task(row["name"], row["description"], row["priority"])
                    self.all_tasks.append(task)
        except FileNotFoundError:
            pass  

def menu():
    todo = ToDoList()
    print('welcome')
    while True:
        print('1. add_task')
        print('2. remove_task')
        print('3. show_list')
        print('4. exit')
        choice = int(input('enter your choice: '))
        if (1 <= choice <= 4):
            if choice == 1:
                name = input("enter task's name: ")
                description = input('description: ')
                priority = input('enter its priority (low-mid-high): ')
                if priority not in ['low', 'mid', 'high']:
                    print(f'{priority} must be either low or mid or high!')
                    return
                task = Task(name, description, priority)
                todo.add_task(task)
            if choice == 2:
                name = input("enter task's name: ")
                todo.remove_task(name)
            if choice == 3:
                todo.show_list()
            if choice == 4:
                print('shutting the program down!')
                break
        else:
            print(f'{choice} is invalid! plaese try again!')

menu()