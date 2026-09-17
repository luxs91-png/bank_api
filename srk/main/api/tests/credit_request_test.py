import pytest

from srk.main.api.models.credit_request_request import CreditRequestRequest
from srk.main.api.models.credit_user_request import CreditUserRequest


@pytest.mark.api
class TestCreditRequest:

    def test_credit_request(self, api_manager, credit_user_request):
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