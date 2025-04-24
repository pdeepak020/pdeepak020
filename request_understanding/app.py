from flask import Flask, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

# In-memory storage (replace with database in production)
tasks = {}

# Helper function to validate task data
def validate_task_data(data):
    required_fields = ['title', 'description']
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"
    return True, None

# GET /api/tasks - Get all tasks
@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify({
        'tasks': list(tasks.values()),
        'count': len(tasks)
    })

# GET /api/tasks/<task_id> - Get a specific task
@app.route('/api/tasks/<task_id>', methods=['GET'])
def get_task(task_id):
    if task_id not in tasks:
        return jsonify({'error': 'Task not found'}), 404
    return jsonify(tasks[task_id])

# POST /api/tasks - Create a new task
@app.route('/api/tasks', methods=['POST'])
def create_task():
    # Check if the request is JSON or form data
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form.to_dict()
        # Convert form data to JSON-like structure
        if 'json' in data:
            del data['json']
    
    # Validate request data
    is_valid, error_message = validate_task_data(data)
    if not is_valid:
        return jsonify({'error': error_message}), 400
    
    # Create new task
    task_id = str(uuid.uuid4())
    task = {
        'id': task_id,
        'title': data['title'],
        'description': data['description'],
        'status': 'pending',
        'created_at': datetime.utcnow().isoformat(),
        'updated_at': datetime.utcnow().isoformat()
    }
    
    tasks[task_id] = task
    return jsonify(task), 201

# PUT /api/tasks/<task_id> - Update a task
@app.route('/api/tasks/<task_id>', methods=['PUT', 'POST'])
def update_task(task_id):
    # Check if this is a POST request with _method=PUT (form submission)
    if request.method == 'POST' and request.form.get('_method') == 'PUT':
        data = request.form.to_dict()
        # Remove form-specific fields
        if '_method' in data:
            del data['_method']
        if 'json' in data:
            del data['json']
    else:
        data = request.get_json()
    
    if task_id not in tasks:
        return jsonify({'error': 'Task not found'}), 404
    
    # Validate request data
    is_valid, error_message = validate_task_data(data)
    if not is_valid:
        return jsonify({'error': error_message}), 400
    
    # Update task
    tasks[task_id].update({
        'title': data['title'],
        'description': data['description'],
        'updated_at': datetime.utcnow().isoformat()
    })
    
    return jsonify(tasks[task_id])

# PATCH /api/tasks/<task_id> - Partially update a task
@app.route('/api/tasks/<task_id>', methods=['PATCH'])
def patch_task(task_id):
    if task_id not in tasks:
        return jsonify({'error': 'Task not found'}), 404
    
    data = request.get_json()
    
    # Update only provided fields
    if 'title' in data:
        tasks[task_id]['title'] = data['title']
    if 'description' in data:
        tasks[task_id]['description'] = data['description']
    if 'status' in data:
        tasks[task_id]['status'] = data['status']
    
    tasks[task_id]['updated_at'] = datetime.utcnow().isoformat()
    
    return jsonify(tasks[task_id])

# DELETE /api/tasks/<task_id> - Delete a task
@app.route('/api/tasks/<task_id>', methods=['DELETE', 'POST'])
def delete_task(task_id):
    # Check if this is a POST request with _method=DELETE (form submission)
    if request.method == 'POST' and request.form.get('_method') == 'DELETE':
        pass  # Continue with deletion
    elif request.method != 'DELETE':
        return jsonify({'error': 'Method not allowed'}), 405
    
    if task_id not in tasks:
        return jsonify({'error': 'Task not found'}), 404
    
    del tasks[task_id]
    return '', 204

# Error handlers
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad request'}), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True) 