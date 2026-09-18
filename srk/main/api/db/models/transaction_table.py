from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from srk.main.api.db.base import Base

class TransactionTable(Base):
    __tablename__ = 'transaction'
    id = Column(Integer, primary_key=True)
    to_account_id = Column(Integer, ForeignKey('account.id'))
    from_account_id = Column(Integer, ForeignKey('account.id'))
    credit_id = Column(Integer, ForeignKey('credit.id'))
    amount = Column(Float)
    transaction_type = Column(String)
    created_at = Column(DateTime, nullable=False)

    def __repr__(self):
        return f'<TransactionTable id: {self.id}>'