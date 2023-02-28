import pytest

from controllers.user_controller import UserController
from schemas.user import User


def test_create_user():
    # Creamos un usuario de prueba
    RFC = 'ABC123456DEF'
    CURP = 'ABC123456DEF123456'
    name = 'Juan Pérez'
    address = 'Calle Falsa 123'
    phone = 1234567890
    email = 'juan.perez@example.com'
    password = 'mipassword'
    user = UserController.create_user(RFC, CURP, name, address, phone, email, password)

    # Verificamos que se haya creado el usuario correctamente
    assert isinstance(user, User)
    assert user.RFC == RFC
    assert user.CURP == CURP
    assert user.name == name
    assert user.address == address
    assert user.phone == phone
    assert user.email == email
    assert user.password == password

    # Verificamos que se haya guardado el usuario en la base de datos
    # (asumiendo que la clase User tiene un método save() que lo guarda en la base de datos)
    assert user.save() is not None
