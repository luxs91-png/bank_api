from dataclasses import dataclass
from enum import Enum

from srk.main.api.models.credit_repay_request import CreditRepayRequest

from srk.main.api.models.credit_repay_response import CreditRepayResponse
from srk.main.api.models.credit_request_request import CreditRequestRequest

from srk.main.api.models.credit_request_response import CreditRequestResponse
from srk.main.api.models.get_account_response import GetAccountResponse
from srk.main.api.models.transfer_account_request import TransferAccountRequest

from srk.main.api.models.transfer_account_response import TransferAccountResponse
from srk.main.api.models.deposit_account_request import DepositAccountRequest
from srk.main.api.models.deposit_account_response import DepositAccountResponse
from srk.main.api.models.create_account_response import CreateAccountResponse
from srk.main.api.models.login_user_response import LoginUserResponse
from srk.main.api.models.login_user_request import LoginUserRequest
from srk.main.api.models.base_model import BaseModel
from typing import Optional, Type

from srk.main.api.models.create_user_request import CreateUserRequest
from srk.main.api.models.create_user_response import CreateUserResponse


@dataclass
class EndpointConfiguration:
    url: str
    request_model: Optional[Type[BaseModel]]
    response_model: Optional[Type[BaseModel]]

class Endpoint(Enum):
    ADMIN_CREATE_USER = EndpointConfiguration(
        request_model=CreateUserRequest,
        url="admin/create",
        response_model=CreateUserResponse
    )

    ADMIN_DELITE_USER = EndpointConfiguration(
        request_model = None,
        url = "admin/users",
        response_model = None

    )

    LOGIN_USER = EndpointConfiguration(
        request_model = LoginUserRequest,
        url = "auth/token/login",
        response_model = LoginUserResponse
    )

    CREATE_ACCOUNT = EndpointConfiguration(
        request_model = None,
        url = "account/create",
        response_model=CreateAccountResponse
    )

    DEPOSIT_ACCOUNT = EndpointConfiguration(
        request_model=DepositAccountRequest,
        url="account/deposit",
        response_model=DepositAccountResponse
    )

    TRANSFER_ACCOUNT = EndpointConfiguration(
        request_model=TransferAccountRequest,
        url="account/transfer",
        response_model=TransferAccountResponse
    )

    GET_ACCOUNT = EndpointConfiguration(
        request_model=None,
        url="account",
        response_model=GetAccountResponse
    )

    CREDIT_REQUEST = EndpointConfiguration(
        request_model=CreditRequestRequest,
        url="credit/request",
        response_model=CreditRequestResponse
    )

    CREDIT_REPAY = EndpointConfiguration(
        request_model=CreditRepayRequest,
        url="credit/repay",
        response_model=CreditRepayResponse
    )