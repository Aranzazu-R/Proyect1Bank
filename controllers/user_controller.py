from schemas.user import User


class UserController:
    @staticmethod
    def create_user(RFC: str, CURP: str, name: str, address: str, phone: int, email: str, password: str) -> User:
        user = User(RFC=RFC, CURP=CURP,
                    name=name, address=address, phone=phone,
                    email=email, password=password)
        user.save()
        return user
