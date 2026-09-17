import pytest

from srk.main.api.models.credit_request_request import CreditRequestRequest
from srk.main.api.models.credit_repay_request import CreditRepayRequest

@pytest.mark.api
class TestCreditRepay:

    def test_credit_repay(self, api_manager, credit_user_request):

        account = api_manager.user_steps.create_account(credit_user_request)

        credit_request = CreditRequestRequest(
            accountId=account.id,
            amount=5000,
            termMonths=12
        )

        credit = api_manager.user_steps.credit_request(
            credit_request,
            credit_user_request
        )

        repay_request = CreditRepayRequest(
            creditId=credit.creditId,
            accountId=account.id,
            amount=5000
        )

        response = api_manager.user_steps.credit_repay(
            repay_request,
            credit_user_request
        )

        assert response.creditId == credit.creditId
        assert response.amountDeposited == 5000