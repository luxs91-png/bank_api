import pytest
from sqlalchemy.orm import Session
from srk.main.api.clases.api_manager import ApiManager
from srk.main.api.db.crud.credit_crud import CreditCrudDb

from srk.main.api.models.credit_request_request import CreditRequestRequest
from srk.main.api.models.credit_user_request import CreditUserRequest


@pytest.mark.api
class TestCreditRequest:

    def test_credit_request(self, api_manager: ApiManager, credit_user_request: CreditUserRequest, db_session: Session):
        account = api_manager.user_steps.create_account(credit_user_request)

        credit_request = CreditRequestRequest(
            accountId=account.id,
            amount=5000,
            termMonths=12
        )

        response = api_manager.user_steps.credit_request(
            credit_request,
            credit_user_request
        )

        assert response.id == account.id
        assert response.amount == 5000
        assert response.termMonths == 12
        assert response.creditId > 0
        credit = CreditCrudDb.get_credit_by_id(db_session,response.creditId)

        assert credit is not None, \
            "После создания кредита запись должна существовать в БД"

        assert credit.account_id == account.id, \
            "В БД должен быть указан правильный account_id"

        assert credit.amount == 5000, \
            "В БД должна быть сохранена правильная сумма кредита"

        assert credit.term_months == 12, \
            "В БД должен быть сохранён правильный срок кредита"