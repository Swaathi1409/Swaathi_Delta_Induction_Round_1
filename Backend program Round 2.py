from flask import Flask, request, jsonify
from uuid import uuid4
from datetime import datetime

app = Flask(__name__)

# Initialize an empty list to store tasks (simulated database)
tasks = []

# Function to generate a unique UUID for each task
def generate_task_id():
    return str(uuid4())

# Endpoint to retrieve all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# Endpoint to retrieve a specific task by ID
@app.route('/tasks/<string:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'message': 'Task not found'}), 404
    return jsonify(task)

# Endpoint to add a new task
@app.route('/add-task', methods=['POST'])
def add_task():
    data = request.json
    if 'name' not in data:
        return jsonify({'message': 'Name is required'}), 400

    new_task = {
        'id': generate_task_id(),
        'name': data['name'],
        'description': data.get('description', ''),
        'deadline': data.get('deadline', None),
        'reminder_time': data.get('reminder_time', None),
        'status': data.get('status', 'Pending'),
        'priority': data.get('priority', 'Medium')
    }
    tasks.append(new_task)
    return jsonify({'message': 'Task added successfully', 'task': new_task}), 201

# Endpoint to update a specific task by ID
@app.route('/update-task/<string:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.json
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'message': 'Task not found'}), 404
    task['name'] = data.get('name', task['name'])
    task['description'] = data.get('description', task['description'])
    task['deadline'] = data.get('deadline', task['deadline'])
    task['reminder_time'] = data.get('reminder_time', task['reminder_time'])
    task['status'] = data.get('status', task['status'])
    task['priority'] = data.get('priority', task['priority'])
    return jsonify({'message': 'Task updated successfully', 'task': task})

# Endpoint to delete a specific task by ID
@app.route('/delete-task/<string:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'message': 'Task not found'}), 404
    tasks.remove(task)
    return jsonify({'message': 'Task deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
