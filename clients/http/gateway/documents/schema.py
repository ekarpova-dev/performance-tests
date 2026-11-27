from pydantic import BaseModel


class DocumentSchema(BaseModel):
    """Описывает JSON-структуру документа."""

    url: str
    document: str


class GetTariffDocumentResponseSchema(BaseModel):
    """Описывает ответ на получение документа тарифа."""

    tariff: DocumentSchema


class GetContractDocumentResponseSchema(BaseModel):
    """Описывает ответ на получение документа контракта."""

    contract: DocumentSchema
