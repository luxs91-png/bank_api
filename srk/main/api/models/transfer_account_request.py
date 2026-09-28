from srk.main.api.generators.creation_rule import CreationRule
from srk.main.api.models.base_model import BaseModel
from typing import Annotated

class TransferAccountRequest(BaseModel):
    fromAccountId: int
    toAccountId: int
    amount: Annotated[int,CreationRule(regex=r"[5-9][0-9]{2}|[1-9][0-9]{3}|10000")]