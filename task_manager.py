from task import Task
from datetime import datetime
import json
import random
import os
class TaskManager:
    tasks = []
    def __init__(self):
        self.load_from_json()
    @staticmethod
    def load_from_json():
        if os.path.exists("task.json"):
            try:
                with open("task.json", "r") as file:
                    data = json.load(file)
                    for item in data:
                        task = Task(item["id"], item["title"], item["description"], item["created_at"])
                        TaskManager.tasks.append(task)
            except:
                TaskManager.tasks = []
        else:
            with open("task.json", "w") as file:
                data = []
                json.dump(data, file, indent = 4)  
    @staticmethod
    def save_to_json():
        data = [task.to_dictionary() for task in TaskManager.tasks]
        with open("task.json", "w") as file:
            json.dump(data, file, indent = 4)
    @staticmethod
    def add_task(title, description):
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_task = Task(id = random.randint(1, 999), title = title, description = description, created_at = created_at)
        TaskManager.tasks.append(new_task)
        print("Task added successfully!")
    @staticmethod
    def view_task():
        if len(TaskManager.tasks) == 0:
            print("No task found.")
        else:
            for task in TaskManager.tasks:
                print(f"id: {task.id}, title: {task.title}, description: {task.description}, created_at: {task.created_at}")
    @staticmethod
    def update_task(task_id, new_title, new_description):
        found = False
        for task in TaskManager.tasks:
            if task_id == task.id:
                found = True
                if new_title != "":
                    task.title = new_title
                if new_description != "":
                    task.description = new_description
        if not found:
            print("task id cannot be found!!!")
    @staticmethod
    def delete_task(task_id):
        found = False
        for task in TaskManager.tasks:
            if task_id == task.id:
                found = True
                TaskManager.tasks.remove(task)
        if not found:
            print("Task ID cannot be found!!!")
    def run(self):
        while True:
            print("===== Student Task Tracker =====")
            print("1. Add New Task")
            print("2. View All Tasks")
            print("3. Update Task")
            print("4. Delete Task")
            print("5. Exit")
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("ValueError!!! Enter a valid choice 1-5")
                continue
            if choice == 1:
                title = input("Enter your task title: ")
                description = input("Enter your task description: ")
                TaskManager.add_task(title, description)
            elif choice == 2:
                TaskManager.view_task()
            elif choice == 3:
                try:
                    task_id = int(input("Enter a valid task id: "))
                except ValueError:
                    print("Invalid task id!!!")
                    continue
                new_title = input("Enter new task title (if you want to update): ")
                new_description = input("Enter new description (if you want to update): ")
                TaskManager.update_task(task_id, new_title, new_description)
            elif choice == 4:
                try:
                    task_id = int(input("Enter a valid task id: "))
                except ValueError:
                    print("Invalid task id!!!")
                    continue
                TaskManager.delete_task(task_id)
            elif choice == 5:
                TaskManager.save_to_json()
                print("Exit from the program.")
                break