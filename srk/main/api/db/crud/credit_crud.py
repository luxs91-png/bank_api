from sqlalchemy.orm import Session
from srk.main.api.db.models.credit_table import Credit

class CreditCrudDb:
    @staticmethod
    def get_credit_by_id(db: Session, credit_id: int) -> Credit | None:
        return db.query(Credit).filter(Credit.id == credit_id).first()
    @staticmethod
    def get_credit_by_account_id(db: Session, account_id: int) -> Credit | None:
        return db.query(Credit).filter(Credit.account_id == account_id).first()