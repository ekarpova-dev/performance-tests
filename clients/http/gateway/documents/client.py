from httpx import Response

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client
from clients.http.gateway.documents.schema import (
    GetTariffDocumentResponseSchema,
    GetContractDocumentResponseSchema,
)


class DocumentsGatewayHTTPClient(HTTPClient):
    """Клиент для взаимодействия с /api/v1/documents сервиса http-gateway."""

    def get_tariff_document_api(self, account_id: str) -> Response:
        """
        Выполняет GET-запрос на получение документа тарифа по счету.

        :param account_id: Идентификатор счета.
        :return: Ответ сервера в формате Response.
        """
        return self.get(f"/api/v1/documents/tariff-document/{account_id}")

    def get_contract_document_api(self, account_id: str) -> Response:
        """
        Выполняет GET-запрос на получение документа контракта по счету.

        :param account_id: Идентификатор счета.
        :return: Ответ сервера в формате Response.
        """
        return self.get(f"/api/v1/documents/contract-document/{account_id}")

    def get_tariff_document(self, account_id: str) -> GetTariffDocumentResponseSchema:
        """
        Получает документ тарифа и возвращает Pydantic-модель ответа.

        :param account_id: Идентификатор счета.
        :return: Модель ответа с документом тарифа.
        """
        response = self.get_tariff_document_api(account_id)
        return GetTariffDocumentResponseSchema.model_validate_json(response.text)

    def get_contract_document(self, account_id: str) -> GetContractDocumentResponseSchema:
        """
        Получает документ контракта и возвращает Pydantic-модель ответа.

        :param account_id: Идентификатор счета.
        :return: Модель ответа с документом контракта.
        """
        response = self.get_contract_document_api(account_id)
        return GetContractDocumentResponseSchema.model_validate_json(response.text)


def build_documents_gateway_http_client() -> DocumentsGatewayHTTPClient:
    """
    Создает настроенный клиент для работы с документами.

    :return: Готовый экземпляр DocumentsGatewayHTTPClient.
    """
    return DocumentsGatewayHTTPClient(client=build_gateway_http_client())
