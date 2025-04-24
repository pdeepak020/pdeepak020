# Flask REST API

A simple REST API built with Flask that demonstrates CRUD operations for a task management system.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

The server will start at `http://localhost:5000`

## API Endpoints

### Tasks

- `GET /api/tasks` - Get all tasks
- `GET /api/tasks/<task_id>` - Get a specific task
- `POST /api/tasks` - Create a new task
- `PUT /api/tasks/<task_id>` - Update a task
- `PATCH /api/tasks/<task_id>` - Partially update a task
- `DELETE /api/tasks/<task_id>` - Delete a task

### Example Usage

1. Create a new task:
```bash
curl -X POST http://localhost:5000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Learn Flask", "description": "Build a REST API with Flask"}'
```

2. Get all tasks:
```bash
curl http://localhost:5000/api/tasks
```

3. Update a task:
```bash
curl -X PUT http://localhost:5000/api/tasks/<task_id> \
  -H "Content-Type: application/json" \
  -d '{"title": "Learn Flask", "description": "Completed building REST API"}'
```

4. Delete a task:
```bash
curl -X DELETE http://localhost:5000/api/tasks/<task_id>
```

## Features

- RESTful API design
- JSON request/response handling
- Input validation
- Error handling
- HTTP status codes
- In-memory storage (can be replaced with a database) 