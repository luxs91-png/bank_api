import requests
from requests import Response

from srk.main.api.models.base_model import BaseModel
from srk.main.api.models.get_account_response import GetAccountResponse
from srk.main.api.request.requester import Requester


class GetAccountRequester(Requester):

    def post(self, model: BaseModel):
        pass

    def get(self, account_id: int) -> GetAccountResponse | Response:
        url = f"{self.base_url}/account/transactions/{account_id}"
        response = requests.get(
            url=url,
            headers=self.headers,
        )
        self.response_spec(response)
        return GetAccountResponse(**response.json())
