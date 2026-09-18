from sqlalchemy.orm import Session

from srk.main.api.db.models.transaction_table import TransactionTable
class TransactionCrudDb:
    @staticmethod
    def get_transaction_by_id(db: Session, transaction_id: int) -> TransactionTable:
        return db.query(TransactionTable).filter(TransactionTable.id == transaction_id).first()

    @staticmethod
    def get_transactions_by_account_id(db: Session, account_id: int) -> list[TransactionTable]:
        return (
            db.query(TransactionTable)
            .filter(
                (TransactionTable.from_account_id == account_id)
                | (TransactionTable.to_account_id == account_id)
            )
            .all()
        )