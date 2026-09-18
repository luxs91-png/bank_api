import pytest
from sqlalchemy.orm import Session
from srk.main.api.clases.api_manager import ApiManager
from srk.main.api.db.crud.transaction_crud import TransactionCrudDb
from srk.main.api.generators.model_generator import RandomModelGenerator
from srk.main.api.models.create_user_request import CreateUserRequest
from srk.main.api.models.deposit_account_request import DepositAccountRequest
from srk.main.api.models.transfer_account_request import TransferAccountRequest


@pytest.mark.api
class TestTransferAccount:
    def test_transfer_account(self, api_manager: ApiManager, create_user_request: CreateUserRequest, db_session: Session):
        second_user_request = RandomModelGenerator.generate(CreateUserRequest)
        api_manager.admin_steps.create_user(second_user_request)

        sender_account = api_manager.user_steps.create_account(create_user_request)
        receiver_account = api_manager.user_steps.create_account(second_user_request)

        api_manager.user_steps.deposit_account(
            DepositAccountRequest(accountId=sender_account.id, amount=1000),
            create_user_request
        )

        transfer_request = TransferAccountRequest(
            fromAccountId=sender_account.id,
            toAccountId=receiver_account.id,
            amount=500
        )

        response = api_manager.user_steps.transfer_account(transfer_request, create_user_request)

        sender_info = api_manager.user_steps.get_account(sender_account.id, create_user_request)
        receiver_info = api_manager.user_steps.get_account(receiver_account.id, second_user_request)

        assert response.fromAccountId == sender_account.id, \
            "В ответе API должен быть ID счёта отправителя"

        assert response.toAccountId == receiver_account.id, \
            "В ответе API должен быть ID счёта получателя"

        assert response.fromAccountIdBalance == 500, \
            "После перевода баланс счёта отправителя должен быть 500"
        assert sender_info.balance == 500
        assert receiver_info.balance == 500

        transactions = TransactionCrudDb.get_transactions_by_account_id(
            db_session,
            sender_account.id
        )
        assert transactions, \
            "После перевода в БД должна существовать хотя бы одна транзакция"

        transaction = next(
            (
                transaction
                for transaction in transactions
                if transaction.from_account_id == sender_account.id
                   and transaction.to_account_id == receiver_account.id
                   and transaction.amount == 500
            ),
            None
        )
        assert transaction is not None, \
            "После перевода транзакция должна быть сохранена в БД"
        assert transaction.from_account_id == sender_account.id, \
            "В БД должен быть указан счёт отправителя"
        assert transaction.to_account_id == receiver_account.id, \
            "В БД должен быть указан счёт получателя"
        assert transaction.amount == 500, \
            "В БД сумма транзакции должна быть равна 500"