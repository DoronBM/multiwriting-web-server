import json
from bottle import route, request
from models.create_user_request import CreateUserRequest
from repositories.users_repository import UsersRepository
from services.users_service import UsersService

repository = UsersRepository()
usersService = UsersService(repository)


@route('/users', method=['GET'])
def get_users():
    users = usersService.get_users()
    print(users)
    return json.dumps(users, default=lambda o: o.__dict__, indent=4)


@route('/users/create', method=['PUT'])
def create_user():
    requestPayload = request.json
    user = CreateUserRequest(
        requestPayload['name'], requestPayload['email'], requestPayload['password'])
    usersService.add_user(user)
    return f'User created'
