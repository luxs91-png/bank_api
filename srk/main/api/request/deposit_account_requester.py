from srk.main.api.models.deposit_account_response import DepositAccountResponse
from srk.main.api.models.deposit_account_request import DepositAccountRequest
from srk.main.api.request.requester import Requester
import requests

class DepositAccountRequester(Requester):
    def post(self,deposit_account_request:DepositAccountRequest) -> DepositAccountResponse:
        url = f"{self.base_url}/account/deposit"
        response = requests.post(
            url=url,
            headers=self.headers,
            json=deposit_account_request.model_dump()
        )
        self.response_spec(response)
        return DepositAccountResponse(**response.json())

