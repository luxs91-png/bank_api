from srk.main.api.models.base_model import BaseModel


class GetAccountResponse(BaseModel):
    id: int
    number: str
    balance: float