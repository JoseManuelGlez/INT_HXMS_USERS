import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

sys.path.insert(0, r'C:\Users\12345\Desktop\ms-users')

from flask import Flask, request, jsonify
from infrastructure.adapters.user_repository_adapter import UserRepositoryAdapter
from domain.models.user_model import UserModel
from domain.uses_cases.user_use_case import UserUseCase

app = Flask(__name__)

user_repository = UserRepositoryAdapter()
user_use_case = UserUseCase(user_repository)

class ApiRest:
    @app.route('/users', methods=['POST'])
    def create_user():
        data: dict = request.get_json()
        user = UserModel(email=data['email'], password=data['password'], name=data['name'], surname=data['surname'])
        return user_use_case.create(user)

    @app.route('/users/login', methods=['POST'])
    def get_user():
        data: dict = request.get_json()
        email = data.get('email')
        password = data.get('password')
        user = user_use_case.get(email, password)
        return jsonify(user.to_dict()) if user else ('', 404)

def start_api():
    app.run(host='0.0.0.0', port=3003, debug=True)

