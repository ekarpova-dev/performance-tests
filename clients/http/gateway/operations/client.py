from httpx import Response, QueryParams

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client
from clients.http.gateway.operations.schema import (
    GetOperationReceiptResponseSchema,
    GetOperationResponseSchema,
    GetOperationsQuerySchema,
    GetOperationsResponseSchema,
    GetOperationsSummaryQuerySchema,
    GetOperationsSummaryResponseSchema,
    MakeBillPaymentOperationRequestSchema,
    MakeBillPaymentOperationResponseSchema,
    MakeCashWithdrawalOperationRequestSchema,
    MakeCashWithdrawalOperationResponseSchema,
    MakeCashbackOperationRequestSchema,
    MakeCashbackOperationResponseSchema,
    MakeFeeOperationRequestSchema,
    MakeFeeOperationResponseSchema,
    MakePurchaseOperationRequestSchema,
    MakePurchaseOperationResponseSchema,
    MakeTopUpOperationRequestSchema,
    MakeTopUpOperationResponseSchema,
    MakeTransferOperationRequestSchema,
    MakeTransferOperationResponseSchema,
    OperationStatus,
)


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

    def get_operations_api(self, query: GetOperationsQuerySchema) -> Response:
        """
        Получает список операций для определенного счета.

        :param query: Query-параметры запроса с идентификатором счета accountId.
        :return: Ответ сервера со списком операций в формате Response.
        """
        return self.get("/api/v1/operations", params=QueryParams(**query.model_dump(by_alias=True)))

    def get_operations_summary_api(self, query: GetOperationsSummaryQuerySchema) -> Response:
        """
        Получает статистику по операциям для определенного счета.

        :param query: Query-параметры запроса с идентификатором счета accountId.
        :return: Ответ сервера со статистикой операций в формате Response.
        """
        return self.get("/api/v1/operations/operations-summary", params=QueryParams(**query.model_dump(by_alias=True)))

    def make_fee_operation_api(self, request: MakeFeeOperationRequestSchema) -> Response:
        """
        Создает операцию комиссии.

        :param request: Тело запроса со status, amount, cardId и accountId.
        :return: Ответ сервера с созданной операцией в формате Response.
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request.model_dump(by_alias=True))

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestSchema) -> Response:
        """
        Создает операцию пополнения.

        :param request: Тело запроса со status, amount, cardId и accountId.
        :return: Ответ сервера с созданной операцией в формате Response.
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request.model_dump(by_alias=True))

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestSchema) -> Response:
        """
        Создает операцию кэшбэка.

        :param request: Тело запроса со status, amount, cardId и accountId.
        :return: Ответ сервера с созданной операцией в формате Response.
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request.model_dump(by_alias=True))

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestSchema) -> Response:
        """
        Создает операцию перевода.

        :param request: Тело запроса со status, amount, cardId и accountId.
        :return: Ответ сервера с созданной операцией в формате Response.
        """
        return self.post("/api/v1/operations/make-transfer-operation", json=request.model_dump(by_alias=True))

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestSchema) -> Response:
        """
        Создает операцию покупки.

        :param request: Тело запроса со status, amount, cardId, accountId и category.
        :return: Ответ сервера с созданной операцией в формате Response.
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request.model_dump(by_alias=True))

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestSchema) -> Response:
        """
        Создает операцию оплаты по счету.

        :param request: Тело запроса со status, amount, cardId и accountId.
        :return: Ответ сервера с созданной операцией в формате Response.
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request.model_dump(by_alias=True))

    def make_cash_withdrawal_operation_api(
        self,
        request: MakeCashWithdrawalOperationRequestSchema,
    ) -> Response:
        """
        Создает операцию снятия наличных денег.

        :param request: Тело запроса со status, amount, cardId и accountId.
        :return: Ответ сервера с созданной операцией в формате Response.
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request.model_dump(by_alias=True))

    def get_operation(self, operation_id: str) -> GetOperationResponseSchema:
        """
        Получает операцию по ее идентификатору.

        :param operation_id: Идентификатор операции.
        :return: Модель ответа с данными операции.
        """
        response = self.get_operation_api(operation_id)
        return GetOperationResponseSchema.model_validate_json(response.text)

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseSchema:
        """
        Получает чек по идентификатору операции.

        :param operation_id: Идентификатор операции.
        :return: Модель ответа с данными чека.
        """
        response = self.get_operation_receipt_api(operation_id)
        return GetOperationReceiptResponseSchema.model_validate_json(response.text)

    def get_operations(self, account_id: str) -> GetOperationsResponseSchema:
        """
        Получает список операций определенного счета.

        :param account_id: Идентификатор счета.
        :return: Модель ответа со списком операций.
        """
        query = GetOperationsQuerySchema(account_id=account_id)
        response = self.get_operations_api(query)
        return GetOperationsResponseSchema.model_validate_json(response.text)

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseSchema:
        """
        Получает статистику операций определенного счета.

        :param account_id: Идентификатор счета.
        :return: Модель ответа со статистикой операций.
        """
        query = GetOperationsSummaryQuerySchema(account_id=account_id)
        response = self.get_operations_summary_api(query)
        return GetOperationsSummaryResponseSchema.model_validate_json(response.text)

    def make_fee_operation(
        self,
        card_id: str,
        account_id: str,
    ) -> MakeFeeOperationResponseSchema:
        """
        Создает операцию комиссии.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Модель ответа с данными созданной операции.
        """
        request = MakeFeeOperationRequestSchema(
            status=OperationStatus.COMPLETED,
            amount=55.77,
            card_id=card_id,
            account_id=account_id,
        )
        response = self.make_fee_operation_api(request)
        return MakeFeeOperationResponseSchema.model_validate_json(response.text)

    def make_top_up_operation(
        self,
        card_id: str,
        account_id: str,
    ) -> MakeTopUpOperationResponseSchema:
        """
        Создает операцию пополнения счета.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Модель ответа с данными созданной операции.
        """
        request = MakeTopUpOperationRequestSchema(
            status=OperationStatus.COMPLETED,
            amount=1500.11,
            card_id=card_id,
            account_id=account_id,
        )
        response = self.make_top_up_operation_api(request)
        return MakeTopUpOperationResponseSchema.model_validate_json(response.text)

    def make_cashback_operation(
        self,
        card_id: str,
        account_id: str,
    ) -> MakeCashbackOperationResponseSchema:
        """
        Создает операцию начисления кэшбэка.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Модель ответа с данными созданной операции.
        """
        request = MakeCashbackOperationRequestSchema(
            status=OperationStatus.COMPLETED,
            amount=25.50,
            card_id=card_id,
            account_id=account_id,
        )
        response = self.make_cashback_operation_api(request)
        return MakeCashbackOperationResponseSchema.model_validate_json(response.text)

    def make_transfer_operation(
        self,
        card_id: str,
        account_id: str,
    ) -> MakeTransferOperationResponseSchema:
        """
        Создает операцию перевода.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Модель ответа с данными созданной операции.
        """
        request = MakeTransferOperationRequestSchema(
            status=OperationStatus.COMPLETED,
            amount=500.50,
            card_id=card_id,
            account_id=account_id,
        )
        response = self.make_transfer_operation_api(request)
        return MakeTransferOperationResponseSchema.model_validate_json(response.text)

    def make_purchase_operation(
        self,
        card_id: str,
        account_id: str,
    ) -> MakePurchaseOperationResponseSchema:
        """
        Создает операцию покупки.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Модель ответа с данными созданной операции.
        """
        request = MakePurchaseOperationRequestSchema(
            status=OperationStatus.COMPLETED,
            amount=77.99,
            card_id=card_id,
            account_id=account_id,
            category="taxi",
        )
        response = self.make_purchase_operation_api(request)
        return MakePurchaseOperationResponseSchema.model_validate_json(response.text)

    def make_bill_payment_operation(
        self,
        card_id: str,
        account_id: str,
    ) -> MakeBillPaymentOperationResponseSchema:
        """
        Создает операцию оплаты по счету.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Модель ответа с данными созданной операции.
        """
        request = MakeBillPaymentOperationRequestSchema(
            status=OperationStatus.COMPLETED,
            amount=250.00,
            card_id=card_id,
            account_id=account_id,
        )
        response = self.make_bill_payment_operation_api(request)
        return MakeBillPaymentOperationResponseSchema.model_validate_json(response.text)

    def make_cash_withdrawal_operation(
        self,
        card_id: str,
        account_id: str,
    ) -> MakeCashWithdrawalOperationResponseSchema:
        """
        Создает операцию снятия наличных денег.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Модель ответа с данными созданной операции.
        """
        request = MakeCashWithdrawalOperationRequestSchema(
            status=OperationStatus.COMPLETED,
            amount=1000.00,
            card_id=card_id,
            account_id=account_id,
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return MakeCashWithdrawalOperationResponseSchema.model_validate_json(response.text)


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Создает настроенный клиент для работы с операциями.

    :return: Готовый экземпляр OperationsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
