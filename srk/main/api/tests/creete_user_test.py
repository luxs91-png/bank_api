
import pytest
from sqlalchemy.orm import Session
from srk.main.api.clases.api_manager import ApiManager
from srk.main.api.generators.model_generator import RandomModelGenerator
from srk.main.api.models.create_user_request import CreateUserRequest
from srk.main.api.db.crud.user_crud import UserCrudDB as User


@pytest.mark.api
class TestCreeteUser:
    @pytest.mark.parametrize(
        "create_user_request",
        [RandomModelGenerator.generate(CreateUserRequest)],
    )
    def test_create_user_valid(self, api_manager:ApiManager, create_user_request:CreateUserRequest, db_session:Session):
        response = api_manager.admin_steps.create_user(create_user_request)

        assert create_user_request.username == response.username
        assert create_user_request.role == response.role

        user_from_db = User.get_user_by_username(db_session, create_user_request.username)
        assert user_from_db.username == create_user_request.username, 'Созданого пользователя нет в бд'

    @pytest.mark.parametrize(
        "username, password",
        [
            ("абв", "Pas!sw0rd"),
            ("ab", "Pas!sw0rd"),
            ("abv!", "Pas!sw0rd"),
            ("Max1", "Pas!sw0rд"),
            ("Max2", "Pas!s"),
            ("Max3", "pas!sw0rd"),
            ("Max4", "PAS!SW0RD"),
            ("Max5", "Passwrd"),

        ]
    )
    def test_create_user_invalid(self, db_session: Session, username: str, password: str, api_manager: ApiManager):
        create_user_request = CreateUserRequest(username=username, password=password, role="ROLE_USER")
        api_manager.admin_steps.create_invalid_user(create_user_request)

        user_from_db = User.get_user_by_username(db_session, create_user_request.username)
        assert user_from_db is None, 'Пользователь создан, ошибка'