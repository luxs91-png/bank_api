from abc import ABC, abstractmethod
from typing import Dict, Callable
from srk.main.api.models.base_model import BaseModel

from srk.main.api.specs import response_specs


class Requester(ABC):
    def __init__(self, request_spec: Dict[str, str], response_spec: Callable):
        self.headers = request_spec["headers"]
        self.base_url = request_spec["base_url"]
        self.response_spec = response_spec

    @abstractmethod
    def post(self, mobel:BaseModel):...