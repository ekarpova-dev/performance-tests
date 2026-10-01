from typing import TypedDict

from httpx import Response, QueryParams

from clients.http.client import HTTPClient


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
