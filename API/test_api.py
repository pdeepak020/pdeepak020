#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Test script for Flask REST API
-----------------------------
This script demonstrates how to interact with the Flask REST API using the requests library.
"""

import requests
import json
import sys

# API base URL
BASE_URL = 'http://localhost:5000/api'

def print_response(response):
    """Print the response in a formatted way"""
    print(f"Status Code: {response.status_code}")
    try:
        print(json.dumps(response.json(), indent=2))
    except:
        print(response.text)

def get_all_tasks():
    """Get all tasks"""
    print("\n=== Getting All Tasks ===")
    response = requests.get(f"{BASE_URL}/tasks")
    print_response(response)
    return response

def get_task(task_id):
    """Get a specific task by ID"""
    print(f"\n=== Getting Task {task_id} ===")
    response = requests.get(f"{BASE_URL}/tasks/{task_id}")
    print_response(response)
    return response

def create_task(title, description):
    """Create a new task"""
    print("\n=== Creating New Task ===")
    data = {
        'title': title,
        'description': description
    }
    response = requests.post(
        f"{BASE_URL}/tasks",
        json=data
    )
    print_response(response)
    return response

def update_task(task_id, title, description):
    """Update a task"""
    print(f"\n=== Updating Task {task_id} ===")
    data = {
        'title': title,
        'description': description
    }
    response = requests.put(
        f"{BASE_URL}/tasks/{task_id}",
        json=data
    )
    print_response(response)
    return response

def delete_task(task_id):
    """Delete a task"""
    print(f"\n=== Deleting Task {task_id} ===")
    response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
    print(f"Status Code: {response.status_code}")
    if response.text:
        print(response.text)
    return response

def main():
    """Main function to demonstrate API usage"""
    print("Flask REST API Test Script")
    print("=========================")
    
    # Create a new task
    create_response = create_task(
        "Learn Flask",
        "Build a REST API with Flask"
    )
    
    # Get the task ID from the response
    if create_response.status_code == 201:
        task_id = create_response.json().get('id')
        
        # Get all tasks
        get_all_tasks()
        
        # Get the specific task
        get_task(task_id)
        
        # Update the task
        update_task(
            task_id,
            "Learn Flask - Updated",
            "Completed building REST API with Flask"
        )
        
        # Delete the task
        delete_task(task_id)
        
        # Verify the task was deleted
        get_task(task_id)
    else:
        print("Failed to create task. Cannot proceed with testing.")

if __name__ == "__main__":
    main() 