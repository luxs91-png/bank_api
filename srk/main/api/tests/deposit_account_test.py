import pytest

from srk.main.api.models.deposit_account_request import DepositAccountRequest


@pytest.mark.api
class TestDepositAccount:
    def test_deposit_account(self, api_manager, create_user_request):
        account = api_manager.user_steps.create_account(create_user_request)

        deposit_request = DepositAccountRequest(
            accountId=account.id,
            amount=1000
        )

        response = api_manager.user_steps.deposit_account(deposit_request, create_user_request)

        assert response.id == account.id
        assert response.balance == 1000