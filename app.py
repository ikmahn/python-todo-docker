from flask import Flask, jsonify, request

app = Flask(__name__)
tasks = []

@app.route('/')
def view_tasks():
    return jsonify({"tasks": tasks})

@app.route('/add', methods=['POST'])
def add_task():
    task = request.json.get('task')
    tasks.append({"task": task, "done": False})
    return jsonify({"message": "Task added!"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)