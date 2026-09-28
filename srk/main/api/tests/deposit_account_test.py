import pytest
from sqlalchemy.orm import Session

from srk.main.api.clases.api_manager import ApiManager
from srk.main.api.db.crud.account_crud import AccountCrudDb
from srk.main.api.generators.model_generator import RandomModelGenerator
from srk.main.api.models.create_user_request import CreateUserRequest
from srk.main.api.models.deposit_account_request import DepositAccountRequest


@pytest.mark.api
class TestDepositAccount:

    def test_deposit_account(self,api_manager: ApiManager,create_user_request: CreateUserRequest,db_session: Session):
        account = api_manager.user_steps.create_account(create_user_request)
        deposit_request = RandomModelGenerator.generate(DepositAccountRequest,accountId=account.id)
        response = api_manager.user_steps.deposit_account(deposit_request,create_user_request)

        assert response.id == account.id, ("В ответе должен быть ID пополняемого счёта")
        assert response.balance == deposit_request.amount, ("Баланс после пополнения должен совпадать с суммой deposit")

        account_from_db = AccountCrudDb.get_account_by_id(db_session,account.id)

        assert account_from_db is not None, ("После создания счёт должен существовать в БД")
        assert account_from_db.id == account.id, ("В БД должен быть правильный ID счёта")
        assert account_from_db.balance == deposit_request.amount, ("Баланс счёта в БД должен совпадать с суммой пополнения")

    @pytest.mark.parametrize(
        "invalid_amount",
        [
            pytest.param(999, id="amount-less-than-min"),
            pytest.param(9001, id="amount-more-than-max"),
        ]
    )
    def test_deposit_invalid_amount(self,api_manager: ApiManager,create_user_request: CreateUserRequest,db_session: Session,invalid_amount: int):
        account = api_manager.user_steps.create_account(create_user_request)

        deposit_request = RandomModelGenerator.generate(DepositAccountRequest,accountId=account.id,amount=invalid_amount)

        api_manager.user_steps.deposit_invalid_account(deposit_request,create_user_request)

        account_from_db = AccountCrudDb.get_account_by_id(db_session,account.id)

        assert account_from_db is not None, ("Счёт должен существовать в БД")

        assert account_from_db.balance == 0, (f"После невалидного пополнения на {invalid_amount} ""баланс счёта не должен измениться")