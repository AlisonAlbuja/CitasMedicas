from flask import Blueprint, request, jsonify
from models import User, db
from utils import verify_admin
from schemas import EditUserSchema

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/edit_user/<int:user_id>', methods=['PUT'])
@verify_admin
def edit_user(user_id):
    data = request.get_json()
    schema = EditUserSchema()
    errors = schema.validate(data)
    if errors:
        return jsonify({'error': errors}), 400

    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    if 'username' in data:
        user.username = data['username']
    if 'email' in data:
        user.email = data['email']

    db.session.commit()
    return jsonify({'message': 'User updated successfully', 'user': {
        'id': user.id,
        'username': user.username,
        'email': user.email
    }}), 200
