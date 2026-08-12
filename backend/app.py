from flask import Flask, jsonify, request
from flask_cors import CORS

from config import Config
from models import Todo, db

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
db.init_app(app)


@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


@app.route("/api/todos", methods=["GET"])
def list_todos():
    todos = Todo.query.order_by(Todo.created_at.desc()).all()
    return jsonify([todo.to_dict() for todo in todos])


@app.route("/api/todos", methods=["POST"])
def create_todo():
    data = request.get_json(silent=True) or {}
    title = (data.get("title") or "").strip()

    if not title:
        return jsonify({"error": "标题不能为空"}), 400

    todo = Todo(title=title)
    db.session.add(todo)
    db.session.commit()
    return jsonify(todo.to_dict()), 201


@app.route("/api/todos/<int:todo_id>", methods=["PATCH"])
def update_todo(todo_id):
    todo = db.session.get(Todo, todo_id)
    if not todo:
        return jsonify({"error": "待办不存在"}), 404

    data = request.get_json(silent=True) or {}
    if "completed" in data:
        todo.completed = bool(data["completed"])
    if "title" in data:
        title = (data.get("title") or "").strip()
        if not title:
            return jsonify({"error": "标题不能为空"}), 400
        todo.title = title

    db.session.commit()
    return jsonify(todo.to_dict())


@app.route("/api/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    todo = db.session.get(Todo, todo_id)
    if not todo:
        return jsonify({"error": "待办不存在"}), 404

    db.session.delete(todo)
    db.session.commit()
    return jsonify({"message": "删除成功"})


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000, debug=True)
