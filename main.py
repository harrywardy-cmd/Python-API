from flask import Flask, request, jsonify
app = Flask(__name__)

# Mock user data storage
users = {
    "1": {"user_id": "1", "name": "John Doe", "email": "john.doe@example.com"},
    "2": {"user_id": "2", "name": "Jane Smith", "email": "jane.smith@example.com"}
}


@app.route("/get-user/<user_id>")   

@app.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    extra = request.args.get("extra")
    if extra:
        user["extra"] = extra

    return jsonify(user), 200

# GET - Retrieve all users
@app.route("/users", methods=["GET"])
def get_all_users():
    return jsonify(list(users.values())), 200

# POST - Create new user
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    if not data or "user_id" not in data:
        return jsonify({"error": "Missing user_id or data"}), 400

    user_id = data["user_id"]
    if user_id in users:
        return jsonify({"error": "User already exists"}), 409

    users[user_id] = data
    return jsonify(data), 201


# PUT - Update existing user
@app.route("/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    users[user_id].update(data)
    return jsonify(users[user_id]), 200


# DELETE - Remove user
@app.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    deleted_user = users.pop(user_id)
    return jsonify({"message": "User deleted", "user": deleted_user}), 200

if __name__ == "__main__":
    app.run(debug=True)     