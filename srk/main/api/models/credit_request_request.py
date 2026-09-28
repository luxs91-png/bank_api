from srk.main.api.models.base_model import BaseModel
from typing import Annotated
from srk.main.api.generators.creation_rule import CreationRule

class CreditRequestRequest(BaseModel):
    accountId: int
    amount: Annotated[int,CreationRule(regex=r"(?:[5-9][0-9]{3}|1[0-4][0-9]{3}|15000)")]
    termMonths: Annotated[int, CreationRule(regex=r"(6|12|18|24)")]