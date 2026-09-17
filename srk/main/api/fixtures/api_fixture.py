import pytest
from srk.main.api.clases.api_manager import ApiManager


@pytest.fixture
def api_manager(created_obj):
    return ApiManager(created_obj)