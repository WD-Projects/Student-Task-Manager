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
                data = json.load("task.json")
                for task in data:
                    TaskManager.tasks.append(task, indent = 4)
            except:
                TaskManager.tasks = []
        else:
            with open("task.json", "w") as file:
                data = []
                json.dump(data, file, indent = 4)  
    @staticmethod
    def save_to_json():
        data = [task.to_dictionary for task in TaskManager.tasks]
        with open("task.json", "w") as file:
            json.dump(data, file, indent = 4)
    @staticmethod
    def add_task(title, description):
        id = random.randint(1, 999)
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_task = Task(id, title, description, created_at)
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
        for task in TaskManager.tasks:
            if task_id == task.id:
                if new_title != "":
                    task.title = new_title
                elif new_description != "":
                    task.description = new_description
        else:
            print("Task ID cannot be found!!!")
    @staticmethod
    def delete_task(task_id):
        for task in TaskManager.tasks:
            if task_id == task.id:
                TaskManager.tasks.remove(task)
        else:
            print("Task ID cannot be found!!!")
    def run(self):
        