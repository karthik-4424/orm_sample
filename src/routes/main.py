from flask import Blueprint, request, jsonify
from src.controllers.home_controller import add_user,get_all_users,delete_user

main = Blueprint('main', __name__)

# Add user route
@main.route('/addUser', methods=['POST'])
def add_user():
    user_data = request.get_json()  

    name = user_data.get('name')

    if name:
        user = add_user(name)
        return jsonify({"id": user.id, "name": user.name}), 201  
    return jsonify({"error": "Name is required"}), 400

#Get User route
@main.route('/getUsers', methods=['GET'])
def get_users():
    users = get_all_users()
    
    if users:
        users_data = [{"id": user.id, "name": user.name} for user in users]
        return jsonify(users_data), 200
    else:
        return jsonify({"message": "No users found"}), 404
    
#Delete User route
@main.route('/deleteUser/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    success = delete_user(user_id)
    if success:
        return jsonify({"message": "User deleted"}), 200
    return jsonify({"error": "User not found"}), 404

