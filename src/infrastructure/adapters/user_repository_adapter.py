import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from typing import List
from domain.models.user_model import UserModel
from domain.repositories.user_repository import UserRepository
from infrastructure.adapters.data_sources.entities.user_entity import UserEntity
from infrastructure.adapters.data_sources.db_config import db
from flask import jsonify
from botocore.exceptions import NoCredentialsError
import boto3

class UserRepositoryAdapter(UserRepository):
    def create(self, user: UserModel, profile_image_path=None):
        new_user = UserEntity(email=user.email, password=user.password, name=user.name, surname=user.surname)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        if profile_image_path:
            self.upload_to_s3(profile_image_path, new_user.id)

        user_dict = {
            'id': new_user.id,
            'email': new_user.email,
            'password': new_user.password,
            'name': new_user.name,
            'surname': new_user.surname
        }
        return jsonify(user_dict), 201

    def get(self, email: str, password: str) -> UserModel:
        return db.query(UserEntity).filter(UserEntity.email == email, UserEntity.password == password).first()
    
    def upload_to_s3(self, file_path, user_id):
        s3_client = boto3.client('s3')
        bucket_name = 'your-bucket-name'
        object_name = f'user-profiles/{user_id}'
        try:
            s3_client.upload_file(file_path, bucket_name, object_name)
            print(f"File {file_path} uploaded to {bucket_name}/{object_name}")
        except FileNotFoundError:
            print("The file was not found")
        except NoCredentialsError:
            print("Credentials not available")
