from typing import TypedDict

from httpx import Response, QueryParams

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


class OperationDict(TypedDict):
    """Описывает структуру банковской операции."""

    id: str
    type: str
    status: str
    amount: float
    cardId: str
    category: str
    createdAt: str
    accountId: str


class OperationReceiptDict(TypedDict):
    """Описывает структуру чека по операции."""

    url: str
    document: str


class OperationsSummaryDict(TypedDict):
    """Описывает статистику операций по счету."""

    spentAmount: float
    receivedAmount: float
    cashbackAmount: float


class GetOperationResponseDict(TypedDict):
    """Описывает ответ на получение операции."""

    operation: OperationDict


class GetOperationReceiptResponseDict(TypedDict):
    """Описывает ответ на получение чека по операции."""

    receipt: OperationReceiptDict


class GetOperationsResponseDict(TypedDict):
    """Описывает ответ со списком операций."""

    operations: list[OperationDict]


class GetOperationsSummaryResponseDict(TypedDict):
    """Описывает ответ со статистикой операций."""

    summary: OperationsSummaryDict


class MakeFeeOperationResponseDict(TypedDict):
    """Описывает ответ на создание операции комиссии."""

    operation: OperationDict


class MakeTopUpOperationResponseDict(TypedDict):
    """Описывает ответ на создание операции пополнения."""

    operation: OperationDict


class MakeCashbackOperationResponseDict(TypedDict):
    """Описывает ответ на создание операции кэшбэка."""

    operation: OperationDict


class MakeTransferOperationResponseDict(TypedDict):
    """Описывает ответ на создание операции перевода."""

    operation: OperationDict


class MakePurchaseOperationResponseDict(TypedDict):
    """Описывает ответ на создание операции покупки."""

    operation: OperationDict


class MakeBillPaymentOperationResponseDict(TypedDict):
    """Описывает ответ на создание операции оплаты по счету."""

    operation: OperationDict


class MakeCashWithdrawalOperationResponseDict(TypedDict):
    """Описывает ответ на создание операции снятия наличных."""

    operation: OperationDict


class GetOperationsQueryDict(TypedDict):
    """
    Query-параметры запроса списка операций.

    :key accountId: Идентификатор счета, для которого нужно получить операции.
    """

    accountId: str


class GetOperationsSummaryQueryDict(TypedDict):
    """
    Query-параметры запроса статистики операций.

    :key accountId: Идентификатор счета, для которого нужно получить статистику.
    """

    accountId: str


class MakeOperationRequestDict(TypedDict):
    """
    Базовая структура тела запроса для создания операции.

    :key status: Статус создаваемой операции.
    :key amount: Сумма операции.
    :key cardId: Идентификатор карты, по которой выполняется операция.
    :key accountId: Идентификатор счета, по которому выполняется операция.
    """

    status: str
    amount: float
    cardId: str
    accountId: str


class MakeFeeOperationRequestDict(MakeOperationRequestDict):
    """
    Структура тела запроса для создания операции комиссии.

    Наследует общие поля операции: status, amount, cardId и accountId.
    """


class MakeTopUpOperationRequestDict(MakeOperationRequestDict):
    """
    Структура тела запроса для создания операции пополнения.

    Наследует общие поля операции: status, amount, cardId и accountId.
    """


class MakeCashbackOperationRequestDict(MakeOperationRequestDict):
    """
    Структура тела запроса для создания операции кэшбэка.

    Наследует общие поля операции: status, amount, cardId и accountId.
    """


class MakeTransferOperationRequestDict(MakeOperationRequestDict):
    """
    Структура тела запроса для создания операции перевода.

    Наследует общие поля операции: status, amount, cardId и accountId.
    """


class MakePurchaseOperationRequestDict(MakeOperationRequestDict):
    """
    Структура тела запроса для создания операции покупки.

    Наследует общие поля операции и дополняет их категорией покупки.

    :key category: Категория покупки.
    """

    category: str


class MakeBillPaymentOperationRequestDict(MakeOperationRequestDict):
    """
    Структура тела запроса для создания операции оплаты по счету.

    Наследует общие поля операции: status, amount, cardId и accountId.
    """


class MakeCashWithdrawalOperationRequestDict(MakeOperationRequestDict):
    """
    Структура тела запроса для создания операции снятия наличных.

    Наследует общие поля операции: status, amount, cardId и accountId.
    """


class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-gateway.

    Содержит методы для получения операций, получения чеков и создания
    операций разных типов через HTTP API.
    """

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Получает информацию об операции по ее идентификатору.

        :param operation_id: Идентификатор операции.
        :return: Ответ сервера с данными операции в формате Response.
        """
        return self.get(f"/api/v1/operations/{operation_id}")

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Получает чек по операции по ее идентификатору.

        :param operation_id: Идентификатор операции.
        :return: Ответ сервера с данными чека в формате Response.
        """
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}")

    def get_operations_api(self, query: GetOperationsQueryDict) -> Response:
        """
        Получает список операций для определенного счета.

        :param query: Query-параметры запроса с идентификатором счета accountId.
        :return: Ответ сервера со списком операций в формате Response.
        """
        return self.get("/api/v1/operations", params=QueryParams(**query))

    def get_operations_summary_api(self, query: GetOperationsSummaryQueryDict) -> Response:
        """
        Получает статистику по операциям для определенного счета.

        :param query: Query-параметры запроса с идентификатором счета accountId.
        :return: Ответ сервера со статистикой операций в формате Response.
        """
        return self.get("/api/v1/operations/operations-summary", params=QueryParams(**query))

    def make_fee_operation_api(self, request: MakeFeeOperationRequestDict) -> Response:
        """
        Создает операцию комиссии.

        :param request: Тело запроса со status, amount, cardId и accountId.
        :return: Ответ сервера с созданной операцией в формате Response.
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestDict) -> Response:
        """
        Создает операцию пополнения.

        :param request: Тело запроса со status, amount, cardId и accountId.
        :return: Ответ сервера с созданной операцией в формате Response.
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestDict) -> Response:
        """
        Создает операцию кэшбэка.

        :param request: Тело запроса со status, amount, cardId и accountId.
        :return: Ответ сервера с созданной операцией в формате Response.
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestDict) -> Response:
        """
        Создает операцию перевода.

        :param request: Тело запроса со status, amount, cardId и accountId.
        :return: Ответ сервера с созданной операцией в формате Response.
        """
        return self.post("/api/v1/operations/make-transfer-operation", json=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """
        Создает операцию покупки.

        :param request: Тело запроса со status, amount, cardId, accountId и category.
        :return: Ответ сервера с созданной операцией в формате Response.
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request)

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestDict) -> Response:
        """
        Создает операцию оплаты по счету.

        :param request: Тело запроса со status, amount, cardId и accountId.
        :return: Ответ сервера с созданной операцией в формате Response.
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)

    def make_cash_withdrawal_operation_api(
        self,
        request: MakeCashWithdrawalOperationRequestDict,
    ) -> Response:
        """
        Создает операцию снятия наличных денег.

        :param request: Тело запроса со status, amount, cardId и accountId.
        :return: Ответ сервера с созданной операцией в формате Response.
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request)

    def get_operation(self, operation_id: str) -> GetOperationResponseDict:
        """
        Получает операцию по ее идентификатору.

        :param operation_id: Идентификатор операции.
        :return: Словарь с данными операции.
        """
        response = self.get_operation_api(operation_id)
        return response.json()

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseDict:
        """
        Получает чек по идентификатору операции.

        :param operation_id: Идентификатор операции.
        :return: Словарь с данными чека.
        """
        response = self.get_operation_receipt_api(operation_id)
        return response.json()

    def get_operations(self, account_id: str) -> GetOperationsResponseDict:
        """
        Получает список операций определенного счета.

        :param account_id: Идентификатор счета.
        :return: Словарь со списком операций.
        """
        query = GetOperationsQueryDict(accountId=account_id)
        response = self.get_operations_api(query)
        return response.json()

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseDict:
        """
        Получает статистику операций определенного счета.

        :param account_id: Идентификатор счета.
        :return: Словарь со статистикой операций.
        """
        query = GetOperationsSummaryQueryDict(accountId=account_id)
        response = self.get_operations_summary_api(query)
        return response.json()

    def make_fee_operation(
        self,
        card_id: str,
        account_id: str,
    ) -> MakeFeeOperationResponseDict:
        """
        Создает операцию комиссии.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Словарь с данными созданной операции.
        """
        request = MakeFeeOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id,
        )
        response = self.make_fee_operation_api(request)
        return response.json()

    def make_top_up_operation(
        self,
        card_id: str,
        account_id: str,
    ) -> MakeTopUpOperationResponseDict:
        """
        Создает операцию пополнения счета.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Словарь с данными созданной операции.
        """
        request = MakeTopUpOperationRequestDict(
            status="COMPLETED",
            amount=1500.11,
            cardId=card_id,
            accountId=account_id,
        )
        response = self.make_top_up_operation_api(request)
        return response.json()

    def make_cashback_operation(
        self,
        card_id: str,
        account_id: str,
    ) -> MakeCashbackOperationResponseDict:
        """
        Создает операцию начисления кэшбэка.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Словарь с данными созданной операции.
        """
        request = MakeCashbackOperationRequestDict(
            status="COMPLETED",
            amount=25.50,
            cardId=card_id,
            accountId=account_id,
        )
        response = self.make_cashback_operation_api(request)
        return response.json()

    def make_transfer_operation(
        self,
        card_id: str,
        account_id: str,
    ) -> MakeTransferOperationResponseDict:
        """
        Создает операцию перевода.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Словарь с данными созданной операции.
        """
        request = MakeTransferOperationRequestDict(
            status="COMPLETED",
            amount=500.50,
            cardId=card_id,
            accountId=account_id,
        )
        response = self.make_transfer_operation_api(request)
        return response.json()

    def make_purchase_operation(
        self,
        card_id: str,
        account_id: str,
    ) -> MakePurchaseOperationResponseDict:
        """
        Создает операцию покупки.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Словарь с данными созданной операции.
        """
        request = MakePurchaseOperationRequestDict(
            status="COMPLETED",
            amount=77.99,
            cardId=card_id,
            accountId=account_id,
            category="taxi",
        )
        response = self.make_purchase_operation_api(request)
        return response.json()

    def make_bill_payment_operation(
        self,
        card_id: str,
        account_id: str,
    ) -> MakeBillPaymentOperationResponseDict:
        """
        Создает операцию оплаты по счету.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Словарь с данными созданной операции.
        """
        request = MakeBillPaymentOperationRequestDict(
            status="COMPLETED",
            amount=250.00,
            cardId=card_id,
            accountId=account_id,
        )
        response = self.make_bill_payment_operation_api(request)
        return response.json()

    def make_cash_withdrawal_operation(
        self,
        card_id: str,
        account_id: str,
    ) -> MakeCashWithdrawalOperationResponseDict:
        """
        Создает операцию снятия наличных денег.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Словарь с данными созданной операции.
        """
        request = MakeCashWithdrawalOperationRequestDict(
            status="COMPLETED",
            amount=1000.00,
            cardId=card_id,
            accountId=account_id,
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return response.json()


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Создает настроенный клиент для работы с операциями.

    :return: Готовый экземпляр OperationsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
