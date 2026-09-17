from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from srk.main.api.db.base import Base

class Credit(Base):
    __tablename__ = 'credit'
    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey('account.id'), nullable=False)
    amount = Column(Float, nullable=False)
    term_month = Column(Integer, nullable=False)
    balance = Column(Float, nullable=False)
    created_at = Column(DateTime, nullable=False)