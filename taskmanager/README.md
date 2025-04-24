# Task Manager

A secure and feature-rich command-line task management application with user authentication, email verification, and task organization capabilities.

## Features

- **User Authentication**
  - Secure user registration with password strength requirements
  - Email verification system
  - Secure login/logout functionality
  - Password hashing using SHA-256

- **Task Management**
  - Create, read, update, and delete tasks
  - Mark tasks as completed
  - Add task descriptions and due dates
  - List all tasks with detailed information
  - User-specific task storage

- **Security Features**
  - Password strength validation
  - Email format validation
  - Secure password storage
  - User session management
  - Data persistence using JSON

## Project Structure

```
taskmanager/
├── src/
│   ├── __init__.py
│   ├── task_manager.py    # Core task management functionality
│   ├── user_manager.py    # User authentication and management
│   └── cli.py            # Command-line interface
├── data/
│   ├── tasks_*.json      # User-specific task storage
│   └── users.json        # User data storage
├── tests/                # Test files
├── requirements.txt      # Project dependencies
└── README.md            # Project documentation
```

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd taskmanager
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Dependencies

The project uses several key dependencies:

- **Core Dependencies**
  - python-dateutil: Advanced date handling
  - pathlib: Cross-platform file path handling
  - typing-extensions: Type hinting support
  - json5: Enhanced JSON support

- **Security**
  - cryptography: Cryptographic operations
  - bcrypt: Secure password hashing

- **Development Tools**
  - pytest: Unit testing
  - black: Code formatting
  - flake8: Code linting
  - mypy: Static type checking

- **Documentation**
  - sphinx: Documentation generation
  - sphinx-rtd-theme: Documentation styling

## Usage

1. Run the application:
   ```bash
   python run.py
   ```

2. Follow the menu prompts:
   ```
   === Task Manager Menu ===
   1. Register
   2. Login
   3. Verify Email
   4. Logout
   5. Add Task
   6. List Tasks
   7. Complete Task
   8. Delete Task
   9. Exit
   ```

3. Registration Process:
   - Choose option 1 to register
   - Enter username and email
   - Create a strong password (requirements shown)
   - Verify email with provided code

4. Task Management:
   - Login with your credentials
   - Add tasks with title, description, and due date
   - List, complete, or delete tasks as needed
   - Logout when finished

## Password Requirements

Passwords must meet the following criteria:
- At least 8 characters long
- Contains at least one uppercase letter
- Contains at least one lowercase letter
- Contains at least one number
- Contains at least one special character (!@#$%^&*(),.?":{}|<>)

## Development

1. Install development dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run tests:
   ```bash
   pytest tests/
   ```

3. Format code:
   ```bash
   black src/
   ```

4. Check types:
   ```bash
   mypy src/
   ```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Future Improvements

- Add task categories/tags
- Implement task priority levels
- Add task reminders
- Create a graphical user interface
- Add task search functionality
- Implement task filtering and sorting
- Add password reset functionality
- Implement email sending for verification codes
- Add session management with timeouts 