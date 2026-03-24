from .task_manager import TaskManagerApp
from .user_manager import PasswordStrengthError

def print_menu():
    print("\n=== Task Manager Menu ===")
    print("1. Register")
    print("2. Login")
    print("3. Verify Email")
    print("4. Logout")
    print("5. Add Task")
    print("6. List Tasks")
    print("7. Complete Task")
    print("8. Delete Task")
    print("9. Exit")
    print("=====================")

def get_input(prompt: str) -> str:
    return input(prompt).strip()

def print_password_requirements():
    print("\nPassword must contain:")
    print("- At least 8 characters")
    print("- At least one uppercase letter")
    print("- At least one lowercase letter")
    print("- At least one number")
    print("- At least one special character (!@#$%^&*(),.?\":{}|<>)")

def main():
    app = TaskManagerApp()
    
    while True:
        print_menu()
        choice = get_input("Enter your choice (1-9): ")
        
        if choice == "1":  # Register
            if app.is_logged_in():
                print("Please logout first to register a new user.")
                continue
                
            username = get_input("Enter username: ")
            print_password_requirements()
            password = get_input("Enter password: ")
            email = get_input("Enter email: ")
            
            try:
                if app.register(username, password, email):
                    print("Registration successful!")
                    print(f"Please check your email for verification code: {app.user_manager.users[username].verification_code}")
                else:
                    print("Username already exists!")
            except PasswordStrengthError as e:
                print(f"Password error: {str(e)}")
            except ValueError as e:
                print(f"Error: {str(e)}")
                
        elif choice == "2":  # Login
            if app.is_logged_in():
                print("You are already logged in!")
                continue
                
            username = get_input("Enter username: ")
            password = get_input("Enter password: ")
            
            try:
                if app.login(username, password):
                    print("Login successful!")
                else:
                    print("Invalid username or password!")
            except ValueError as e:
                print(f"Error: {str(e)}")
                
        elif choice == "3":  # Verify Email
            if app.is_logged_in():
                print("You are already logged in!")
                continue
                
            username = get_input("Enter username: ")
            code = get_input("Enter verification code: ")
            
            if app.user_manager.verify_email(username, code):
                print("Email verified successfully! You can now login.")
            else:
                print("Invalid verification code!")
                
        elif choice == "4":  # Logout
            if not app.is_logged_in():
                print("You are not logged in!")
                continue
                
            app.logout()
            print("Logged out successfully!")
            
        elif choice == "5":  # Add Task
            if not app.is_logged_in():
                print("Please login first!")
                continue
                
            title = get_input("Enter task title: ")
            description = get_input("Enter task description: ")
            due_date = get_input("Enter due date (YYYY-MM-DD) or press Enter to skip: ")
            
            app.task_manager.add_task(title, description, due_date if due_date else None)
            print("Task added successfully!")
            
        elif choice == "6":  # List Tasks
            if not app.is_logged_in():
                print("Please login first!")
                continue
                
            tasks = app.task_manager.list_tasks()
            if not tasks:
                print("No tasks found!")
            else:
                print("\nYour tasks:")
                for i, task in enumerate(tasks):
                    print(f"{i}. {task.title} - {'Completed' if task.completed else 'Pending'}")
                    if task.description:
                        print(f"   Description: {task.description}")
                    if task.due_date:
                        print(f"   Due date: {task.due_date}")
                        
        elif choice == "7":  # Complete Task
            if not app.is_logged_in():
                print("Please login first!")
                continue
                
            try:
                index = int(get_input("Enter task number to complete: "))
                app.task_manager.complete_task(index)
                print("Task marked as completed!")
            except (ValueError, IndexError):
                print("Invalid task number!")
                
        elif choice == "8":  # Delete Task
            if not app.is_logged_in():
                print("Please login first!")
                continue
                
            try:
                index = int(get_input("Enter task number to delete: "))
                app.task_manager.delete_task(index)
                print("Task deleted successfully!")
            except (ValueError, IndexError):
                print("Invalid task number!")
                
        elif choice == "9":  # Exit
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main() 