import pytest
from sqlalchemy.orm import Session

from srk.main.api.generators.model_generator import RandomModelGenerator
from srk.main.api.clases.api_manager import ApiManager
from srk.main.api.db.crud.credit_crud import CreditCrudDb

from srk.main.api.models.credit_request_request import CreditRequestRequest
from srk.main.api.models.credit_user_request import CreditUserRequest


@pytest.mark.api
class TestCreditRequest:

    def test_credit_request(self, api_manager: ApiManager, credit_user_request: CreditUserRequest, db_session: Session):
        account = api_manager.user_steps.create_account(credit_user_request)

        credit_request = RandomModelGenerator.generate(
            CreditRequestRequest,
            accountId=account.id
        )

        response = api_manager.user_steps.credit_request(
            credit_request,
            credit_user_request
        )

        assert response.id == credit_request.accountId
        assert response.amount == credit_request.amount
        assert response.termMonths == credit_request.termMonths
        assert response.creditId > 0
        credit = CreditCrudDb.get_credit_by_id(db_session,response.creditId)

        assert credit is not None, \
            "После создания кредита запись должна существовать в БД"
        assert credit.account_id == credit_request.accountId, \
            "В БД должен быть указан правильный account_id"
        assert credit.amount == credit_request.amount, \
            "В БД должна быть сохранена сумма из запроса"
        assert credit.term_months == credit_request.termMonths, \
            "В БД должен быть сохранён срок кредита из запроса"

    @pytest.mark.parametrize(
        "invalid_amount",
        [
            pytest.param(4999, id="credit-amount-less-than-min"),
            pytest.param(15001, id="credit-amount-more-than-max"),
        ]
    )
    def test_credit_request_invalid_amount(
            self,
            api_manager: ApiManager,
            credit_user_request: CreditUserRequest,
            db_session: Session,
            invalid_amount: int
    ):
        account = api_manager.user_steps.create_account(
            credit_user_request
        )

        credit_request = RandomModelGenerator.generate(
            CreditRequestRequest,
            accountId=account.id,
            amount=invalid_amount
        )

        api_manager.user_steps.credit_invalid_request(
            credit_request,
            credit_user_request
        )

        credit_from_db = CreditCrudDb.get_credit_by_account_id(
            db_session,
            account.id
        )

        assert credit_from_db is None, (
            f"Кредит с невалидной суммой {invalid_amount} "
            "не должен сохраняться в БД"
        )