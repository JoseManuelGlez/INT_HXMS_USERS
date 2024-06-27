import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from typing import List
from domain.models.user_model import UserModel
from domain.repositories.user_repository import UserRepository

class UserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create(self, user: UserModel) -> UserModel:
        return self.user_repository.create(user)

    def get(self, email: str, password: str) -> UserModel:
        return self.user_repository.get(email, password)