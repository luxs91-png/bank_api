import pytest
from sqlalchemy.orm import Session

from srk.main.api.clases.api_manager import ApiManager
from srk.main.api.db.crud.credit_crud import CreditCrudDb
from srk.main.api.generators.model_generator import RandomModelGenerator
from srk.main.api.models.credit_request_request import CreditRequestRequest
from srk.main.api.models.credit_repay_request import CreditRepayRequest
from srk.main.api.models.credit_user_request import CreditUserRequest


@pytest.mark.api
class TestCreditRepay:

    def test_credit_repay(
        self,
        api_manager: ApiManager,
        credit_user_request: CreditUserRequest,
        db_session: Session
    ):
        account = api_manager.user_steps.create_account(
            credit_user_request
        )

        credit_request = RandomModelGenerator.generate(
            CreditRequestRequest,
            accountId=account.id
        )

        credit = api_manager.user_steps.credit_request(
            credit_request,
            credit_user_request
        )

        repay_request = RandomModelGenerator.generate(
            CreditRepayRequest,
            creditId=credit.creditId,
            accountId=account.id,
            amount=credit_request.amount
        )

        response = api_manager.user_steps.credit_repay(
            repay_request,
            credit_user_request
        )

        assert response.creditId == credit.creditId, (
            "В ответе должен быть ID погашаемого кредита"
        )

        assert response.amountDeposited == repay_request.amount, (
            "Сумма погашения должна совпадать с отправленной суммой"
        )

        credit_after_repay = CreditCrudDb.get_credit_by_id(
            db_session,
            credit.creditId
        )

        assert credit_after_repay is not None, (
            "После погашения кредита запись должна существовать в БД"
        )

        assert credit_after_repay.account_id == account.id, (
            "После погашения у кредита должен сохраниться правильный account_id"
        )

        assert credit_after_repay.balance == 0, (
            "После полного погашения balance кредита должен быть равен 0"
        )

    def test_credit_repay_partial_amount(
            self,
            api_manager: ApiManager,
            credit_user_request: CreditUserRequest,
            db_session: Session
    ):
        account = api_manager.user_steps.create_account(
            credit_user_request
        )

        credit_request = RandomModelGenerator.generate(
            CreditRequestRequest,
            accountId=account.id
        )

        credit = api_manager.user_steps.credit_request(
            credit_request,
            credit_user_request
        )

        credit_before_repay = CreditCrudDb.get_credit_by_id(
            db_session,
            credit.creditId
        )

        assert credit_before_repay is not None, (
            "Созданный кредит должен существовать в БД"
        )

        balance_before_repay = credit_before_repay.balance

        partial_amount = credit_request.amount - 1

        repay_request = RandomModelGenerator.generate(
            CreditRepayRequest,
            creditId=credit.creditId,
            accountId=account.id,
            amount=partial_amount
        )

        api_manager.user_steps.credit_repay_invalid(
            repay_request,
            credit_user_request
        )

        db_session.expire_all()

        credit_after_repay = CreditCrudDb.get_credit_by_id(
            db_session,
            credit.creditId
        )

        assert credit_after_repay is not None, (
            "После невалидного погашения кредит должен остаться в БД"
        )

        assert credit_after_repay.balance == balance_before_repay, (
            "При частичном погашении баланс кредита не должен изменяться"
        )