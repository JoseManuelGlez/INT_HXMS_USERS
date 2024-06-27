import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from typing import List
from abc import ABC, abstractmethod
from domain.models.user_model import UserModel

class UserRepository(ABC):
    @abstractmethod
    def create(self, user: UserModel) -> UserModel:
        pass

    @abstractmethod
    def get(self, email: str, password: str) -> UserModel:
        pass
