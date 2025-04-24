import json
import os
from datetime import datetime
from typing import List, Dict
from .user_manager import UserManager, User

class Task:
    def __init__(self, title: str, description: str = "", due_date: str = None):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.created_at = datetime.now().isoformat()
        self.completed = False

    def to_dict(self) -> Dict:
        return {
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "created_at": self.created_at,
            "completed": self.completed
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Task':
        task = cls(data["title"], data["description"], data["due_date"])
        task.created_at = data["created_at"]
        task.completed = data["completed"]
        return task

class TaskManager:
    def __init__(self, user: User):
        self.user = user
        self.file_path = f"data/tasks_{user.username}.json"
        self.tasks: List[Task] = []
        # Create data directory if it doesn't exist
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.file_path, 'r') as f:
                tasks_data = json.load(f)
                self.tasks = [Task.from_dict(task_data) for task_data in tasks_data]
        except FileNotFoundError:
            self.tasks = []
            self.save_tasks()

    def save_tasks(self):
        with open(self.file_path, 'w') as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=4)

    def add_task(self, title: str, description: str = "", due_date: str = None) -> Task:
        task = Task(title, description, due_date)
        self.tasks.append(task)
        self.save_tasks()
        return task

    def get_task(self, index: int) -> Task:
        if 0 <= index < len(self.tasks):
            return self.tasks[index]
        raise IndexError("Task index out of range")

    def complete_task(self, index: int):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            self.save_tasks()
        else:
            raise IndexError("Task index out of range")

    def delete_task(self, index: int):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()
        else:
            raise IndexError("Task index out of range")

    def list_tasks(self) -> List[Task]:
        return self.tasks

class TaskManagerApp:
    def __init__(self):
        self.user_manager = UserManager()
        self.current_user = None
        self.task_manager = None

    def register(self, username: str, password: str, email: str) -> bool:
        """Register a new user"""
        return self.user_manager.register(username, password, email)

    def login(self, username: str, password: str) -> bool:
        """Login a user"""
        user = self.user_manager.login(username, password)
        if user:
            self.current_user = user
            self.task_manager = TaskManager(user)
            return True
        return False

    def logout(self):
        """Logout the current user"""
        self.current_user = None
        self.task_manager = None

    def is_logged_in(self) -> bool:
        """Check if a user is currently logged in"""
        return self.current_user is not None

if __name__ == "__main__":
    # Example usage
    app = TaskManagerApp()
    
    # Register a new user
    if app.register("testuser", "password123", "test@example.com"):
        print("User registered successfully!")
    
    # Login
    if app.login("testuser", "password123"):
        print("Logged in successfully!")
        
        # Add some sample tasks
        app.task_manager.add_task("Complete project", "Finish the task manager project", "2024-04-10")
        app.task_manager.add_task("Buy groceries", "Get milk and bread", "2024-04-07")
        
        # List all tasks
        print("\nAll tasks:")
        for i, task in enumerate(app.task_manager.list_tasks()):
            print(f"{i}. {task.title} - {'Completed' if task.completed else 'Pending'}")
    else:
        print("Login failed!") 