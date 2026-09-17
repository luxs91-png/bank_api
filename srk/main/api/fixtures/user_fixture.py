import pytest
from srk.main.api.models.create_user_request import CreateUserRequest
from srk.main.api.models.credit_user_request import CreditUserRequest
from srk.main.api.generators.model_generator import RandomModelGenerator


@pytest.fixture
def create_user_request(api_manager):
    user_request = RandomModelGenerator.generate(CreateUserRequest)
    api_manager.admin_steps.create_user(user_request)
    return user_request


@pytest.fixture
def credit_user_request(api_manager):
    user_request = RandomModelGenerator.generate(CreditUserRequest)
    api_manager.admin_steps.create_credit_user(user_request)
    return user_request