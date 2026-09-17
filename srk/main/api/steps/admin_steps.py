from srk.main.api.models.credit_user_request import CreditUserRequest
from srk.main.api.models.login_user_request import LoginUserRequest
from srk.main.api.foundation.endpoint import Endpoint
from srk.main.api.foundation.requesters.crud_requester import CrudRequester
from srk.main.api.foundation.requesters.validate_crud_requester import ValidateCrudRequester
from srk.main.api.steps.base_steps import BaseSteps
from srk.main.api.models.create_user_request import CreateUserRequest
from srk.main.api.specs.response_specs import ResponseSpecs
from srk.main.api.specs.request_specs import RequestSpecs


class AdminSteps(BaseSteps):
    def create_user(self, create_user_request: CreateUserRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username="admin", password="123456"),
            Endpoint.ADMIN_CREATE_USER,
            ResponseSpecs.requests_ok()
        ).post(create_user_request)

        self.created_obj.append(response)
        return response

    def create_credit_user(self, credit_user_request: CreditUserRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username="admin", password="123456"),
            Endpoint.ADMIN_CREATE_USER,
            ResponseSpecs.requests_ok()
        ).post(credit_user_request)

        self.created_obj.append(response)
        return response


    def delete_user(self, user_id: int):
        CrudRequester(
            RequestSpecs.auth_headers(username="admin", password="123456"),
            Endpoint.ADMIN_DELITE_USER,
            ResponseSpecs.requests_ok()
        ).delete(user_id)

    def create_invalid_user(self, create_user_request: CreateUserRequest):
        CrudRequester(
            RequestSpecs.auth_headers(username="admin", password="123456"),
            Endpoint.ADMIN_CREATE_USER,
            ResponseSpecs.requests_bad()
        ).post(create_user_request)

    def login_user(self, Login_user_request: LoginUserRequest):
        response = ValidateCrudRequester(
            RequestSpecs.unauth_headers(),
            Endpoint.LOGIN_USER,
            ResponseSpecs.requests_ok()
        ).post(Login_user_request)
        return response