
from srk.main.api.models.credit_request_response import CreditRequestResponse
from srk.main.api.models.credit_request_request import CreditRequestRequest
import requests
from srk.main.api.request.requester import Requester


class CreditRequestRequestesr(Requester):
    def post(self, credit_request_request: CreditRequestRequest) -> CreditRequestResponse:
        url=f"{self.base_url}/credit/request"
        response = requests.post(
            url=url,
            headers=self.headers,
            json=credit_request_request.model_dump()
        )
        self.response_spec(response)
        return CreditRequestResponse(**response.json())