
from entities.user import User
from models.user_response import UserResponse
from models.create_user_request import CreateUserRequest
from repositories.users_repository import UsersRepository


class UsersService:
    def __init__(self, userRepository: UsersRepository):
        self.repository = userRepository

    def get_users(self) -> list[UserResponse]:
        users = self.repository.get_all()
        response = []
        for user in users:
            response.append(UserResponse(user.id, user.name, user.email))
        return response

    def add_user(self, createUserRequest: CreateUserRequest) -> None:
        self.repository.store_user(User(-1,
                                        createUserRequest.name, createUserRequest.email, createUserRequest.password))
