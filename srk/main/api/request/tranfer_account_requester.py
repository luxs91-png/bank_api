from requests import Response

import requests

from srk.main.api.configs.config import Config
from srk.main.api.foundation.requesters.crud_requester import CrudRequester
from srk.main.api.models.transfer_account_request import TransferAccountRequest
from srk.main.api.models.transfer_account_response import TransferAccountResponse
from srk.main.api.request.requester import Requester


class TransferAccountRequester(Requester):
    def post(self, transfer_account_request: TransferAccountRequest) -> TransferAccountResponse | Response:
        url = f"{self.base_url}/account/transfer"
        response = requests.post(
            url=url,
            headers=self.headers,
            json=transfer_account_request.model_dump(),
        )
        self.response_spec(response)
        return TransferAccountResponse(**response.json())
