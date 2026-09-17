from srk.main.api.models.credit_repay_request import CreditRepayRequest
from srk.main.api.request.get_account_requester import GetAccountRequester
from srk.main.api.models.transfer_account_request import TransferAccountRequest
from srk.main.api.models.deposit_account_request import DepositAccountRequest
from srk.main.api.specs.response_specs import ResponseSpecs
from srk.main.api.foundation.endpoint import Endpoint
from srk.main.api.specs.request_specs import RequestSpecs
from srk.main.api.foundation.requesters.validate_crud_requester import ValidateCrudRequester
from srk.main.api.models.create_user_request import CreateUserRequest
from srk.main.api.steps.base_steps import BaseSteps
from srk.main.api.configs.config import Config
from srk.main.api.models.credit_request_request import CreditRequestRequest


class UserSteps(BaseSteps):
    def create_account(self, create_user_request: CreateUserRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.CREATE_ACCOUNT,
            ResponseSpecs.requests_create()
        ).post()
        return response

    def deposit_account(self, deposit_account_request, create_user_request: CreateUserRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(
                username=create_user_request.username,
                password=create_user_request.password
            ),
            Endpoint.DEPOSIT_ACCOUNT,
            ResponseSpecs.requests_ok()
        ).post(deposit_account_request)

        return response

    def transfer_account(self, transfer_account_request: TransferAccountRequest, create_user_request: CreateUserRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(
                username=create_user_request.username,
                password=create_user_request.password
            ),
            Endpoint.TRANSFER_ACCOUNT,
            ResponseSpecs.requests_ok()
        ).post(transfer_account_request)

        return response

    def get_account(self, account_id: int, create_user_request: CreateUserRequest):
        request_spec = {
            "headers": RequestSpecs.auth_headers(
                username=create_user_request.username,
                password=create_user_request.password
            ),
            "base_url": Config.fetch("backendURL")
        }

        response = GetAccountRequester(
            request_spec=request_spec,
            response_spec=ResponseSpecs.requests_ok()
        ).get(account_id)

        return response

    def credit_request(
            self,
            credit_request_request: CreditRequestRequest,
            create_user_request: CreateUserRequest
    ):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(
                username=create_user_request.username,
                password=create_user_request.password
            ),
            Endpoint.CREDIT_REQUEST,
            ResponseSpecs.requests_create()
        ).post(credit_request_request)

        return response

    def credit_repay(
            self,
            credit_repay_request: CreditRepayRequest,
            create_user_request: CreateUserRequest
    ):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(
                username=create_user_request.username,
                password=create_user_request.password
            ),
            Endpoint.CREDIT_REPAY,
            ResponseSpecs.requests_ok()
        ).post(credit_repay_request)

        return response