from typing import TypedDict

from httpx import Response

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


class DocumentDict(TypedDict):
    """Описывает JSON-структуру документа."""

    url: str
    document: str


class GetTariffDocumentResponseDict(TypedDict):
    """Описывает ответ на получение документа тарифа."""

    tariff: DocumentDict


class GetContractDocumentResponseDict(TypedDict):
    """Описывает ответ на получение документа контракта."""

    contract: DocumentDict


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

    def get_tariff_document(self, account_id: str) -> GetTariffDocumentResponseDict:
        """
        Получает документ тарифа и возвращает его JSON-представление.

        :param account_id: Идентификатор счета.
        :return: Словарь с документом тарифа.
        """
        response = self.get_tariff_document_api(account_id)
        return response.json()

    def get_contract_document(self, account_id: str) -> GetContractDocumentResponseDict:
        """
        Получает документ контракта и возвращает его JSON-представление.

        :param account_id: Идентификатор счета.
        :return: Словарь с документом контракта.
        """
        response = self.get_contract_document_api(account_id)
        return response.json()


def build_documents_gateway_http_client() -> DocumentsGatewayHTTPClient:
    """
    Создает настроенный клиент для работы с документами.

    :return: Готовый экземпляр DocumentsGatewayHTTPClient.
    """
    return DocumentsGatewayHTTPClient(client=build_gateway_http_client())
