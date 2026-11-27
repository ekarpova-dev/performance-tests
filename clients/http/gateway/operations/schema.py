from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field


class OperationType(StrEnum):
    FEE = "FEE"
    TOP_UP = "TOP_UP"
    PURCHASE = "PURCHASE"
    CASHBACK = "CASHBACK"
    TRANSFER = "TRANSFER"
    BILL_PAYMENT = "BILL_PAYMENT"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"


class OperationStatus(StrEnum):
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    UNSPECIFIED = "UNSPECIFIED"


class OperationSchema(BaseModel):
    """Описывает структуру банковской операции."""
    model_config = ConfigDict(populate_by_name=True)

    id: str
    type: OperationType
    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    category: str
    created_at: datetime = Field(alias="createdAt")
    account_id: str = Field(alias="accountId")



class OperationReceiptSchema(BaseModel):
    """Описывает структуру чека по операции."""

    url: str
    document: str



class OperationsSummarySchema(BaseModel):
    """Описывает статистику операций по счету."""
    model_config = ConfigDict(populate_by_name=True)

    spent_amount: float = Field(alias="spentAmount")
    received_amount: float = Field(alias="receivedAmount")
    cashback_amount: float = Field(alias="cashbackAmount")


class GetOperationResponseSchema(BaseModel):
    """Описывает ответ на получение операции."""

    operation: OperationSchema


class GetOperationReceiptResponseSchema(BaseModel):
    """Описывает ответ на получение чека по операции."""

    receipt: OperationReceiptSchema


class GetOperationsResponseSchema(BaseModel):
    """Описывает ответ со списком операций."""

    operations: list[OperationSchema]


class GetOperationsSummaryResponseSchema(BaseModel):
    """Описывает ответ со статистикой операций."""

    summary: OperationsSummarySchema


class MakeFeeOperationResponseSchema(BaseModel):
    """Описывает ответ на создание операции комиссии."""

    operation: OperationSchema


class MakeTopUpOperationResponseSchema(BaseModel):
    """Описывает ответ на создание операции пополнения."""

    operation: OperationSchema


class MakeCashbackOperationResponseSchema(BaseModel):
    """Описывает ответ на создание операции кэшбэка."""

    operation: OperationSchema


class MakeTransferOperationResponseSchema(BaseModel):
    """Описывает ответ на создание операции перевода."""

    operation: OperationSchema


class MakePurchaseOperationResponseSchema(BaseModel):
    """Описывает ответ на создание операции покупки."""

    operation: OperationSchema


class MakeBillPaymentOperationResponseSchema(BaseModel):
    """Описывает ответ на создание операции оплаты по счету."""

    operation: OperationSchema


class MakeCashWithdrawalOperationResponseSchema(BaseModel):
    """Описывает ответ на создание операции снятия наличных."""

    operation: OperationSchema


class GetOperationsQuerySchema(BaseModel):
    """
    Query-параметры запроса списка операций.

    :key accountId: Идентификатор счета, для которого нужно получить операции.
    """
    model_config = ConfigDict(populate_by_name=True)
    account_id: str = Field(alias="accountId")


class GetOperationsSummaryQuerySchema(BaseModel):
    """
    Query-параметры запроса статистики операций.

    :key accountId: Идентификатор счета, для которого нужно получить статистику.
    """

    model_config = ConfigDict(populate_by_name=True)
    account_id: str = Field(alias="accountId")


class MakeOperationRequestSchema(BaseModel):
    """
    Базовая структура тела запроса для создания операции.

    :key status: Статус создаваемой операции.
    :key amount: Сумма операции.
    :key cardId: Идентификатор карты, по которой выполняется операция.
    :key accountId: Идентификатор счета, по которому выполняется операция.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeFeeOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура тела запроса для создания операции комиссии.

    Наследует общие поля операции: status, amount, cardId и accountId.
    """


class MakeTopUpOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура тела запроса для создания операции пополнения.

    Наследует общие поля операции: status, amount, cardId и accountId.
    """


class MakeCashbackOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура тела запроса для создания операции кэшбэка.

    Наследует общие поля операции: status, amount, cardId и accountId.
    """


class MakeTransferOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура тела запроса для создания операции перевода.

    Наследует общие поля операции: status, amount, cardId и accountId.
    """


class MakePurchaseOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура тела запроса для создания операции покупки.

    Наследует общие поля операции и дополняет их категорией покупки.

    :key category: Категория покупки.
    """

    category: str


class MakeBillPaymentOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура тела запроса для создания операции оплаты по счету.

    Наследует общие поля операции: status, amount, cardId и accountId.
    """


class MakeCashWithdrawalOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура тела запроса для создания операции снятия наличных.

    Наследует общие поля операции: status, amount, cardId и accountId.
    """
