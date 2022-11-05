from entities.user import User


class UsersRepository:
    def __init__(self) -> None:
        user1 = User(1, "Doron", "doron@gmail.com", "****")
        user2 = User(2, "bilbo", "bilbo@gmail.com", "****")
        self.users = [user1, user2]

    def get_all(self) -> list[User]:
        return self.users

    def store_user(self, user: User) -> None:
        self.users.append(user)
