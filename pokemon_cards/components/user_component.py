from typing import Dict, Any, List

from flask_restful import abort

from pokemon_cards.models import User
from pokemon_cards.repositories.user_repository import UserRepository


class UserComponent(object):
    def __init__(self):
        self.repository = UserRepository()

    def get_all(self) -> List[User]:
        """
        Get all Users

        :return:
        """
        users = self.repository.get_records()
        return users

    def get_users_by_name(self, name: str):
        """
        Get users by name

        :param name:
        :return:
        """
        user = self.repository.get_users_by_name(name=name)
        return user

    def get_by_email(self, user_email: str):
        """
        Get user by email

        :param user_email:
        :return:
        """
        user = self.repository.get_user_by_email(user_email=user_email)
        return user

    def get_by_id(self, user_id: int):
        """
        Get user by id

        :param user_id:
        :return:
        """
        user = self.repository.get_by_id(record_id=user_id)
        return user

    def create_user(self, data: Dict[str, Any]) -> User:
        """
        Create a new User

        :param data:
        :return:
        """
        create_data = self.__prepare_creation_data(data=data)
        user = self.repository.create_record(create_data=create_data)
        return user

    def update_user(self, user_id: int, data: Dict[str, Any]) -> int:
        """
        Update a user

        :param user_id:
        :param data:
        :return:
        """
        count = 0
        update_data = self.__prepare_update_data(data=data)
        if update_data:
            self._check_user_exists(user_id=user_id)
            count = self.repository.update_record(record_id=user_id, update_data=update_data)
        return count

    def delete_user(self, user_id: int) -> int:
        """
        Delete a user

        :param user_id:
        :return:
        """
        self._check_user_exists(user_id=user_id)
        count = self.repository.delete_record(record_id=user_id)
        return count

    def _check_user_exists(self, user_id: int) -> User:
        """
        Check if the user exists, if not, will return 404

        :param user_id:
        :return:
        """
        user = self.get_by_id(user_id=user_id)
        if not user:
            abort(404, message=f"User {user_id} doesn't exist")
        return user

    def __prepare_creation_data(self, data: Dict) -> Dict:
        create_data = {}
        if User.email.key in data:
            create_data[User.email.key] = data[User.email.key]
        if User.name.key in data:
            create_data[User.name.key] = data[User.name.key]
        if User.bio.key in data:
            create_data[User.bio.key] = data[User.bio.key]

        if not create_data and [User.email.key, User.name.key] not in create_data:
            abort(422, message=f"Unprocessable Entity, Creation failed. Missing data!")

        return create_data

    def __prepare_update_data(self, data: Dict) -> Dict:
        update_data = {}
        if User.name.key in data:
            update_data[User.name.key] = data[User.name.key]
        if User.bio.key in data:
            update_data[User.bio.key] = data[User.bio.key]

        return update_data
