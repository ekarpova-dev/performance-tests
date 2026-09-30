from typing import TypedDict

from httpx import Response

from clients.http.client import HTTPClient


class IssueVirtualCardRequestDict(TypedDict):
    """
    Структура данных для выпуска виртуальной карты.
    """
    userId: str
    accountId: str


class IssuePhysicalCardRequestDict(TypedDict):
    """
    Структура данных для выпуска физической карты.
    """
    userId: str
    accountId: str


class CardsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/cards сервиса http-gateway.
    """

    def issue_virtual_card_api(self, request: IssueVirtualCardRequestDict) -> Response:
        """
        Выпускает новую виртуальную карту.

        :param request: Данные для выпуска карты: userId и accountId.
        :return: Ответ сервера с данными выпущенной карты в формате Response.
        """
        return self.post("/api/v1/cards/issue-virtual-card", json=request)

    def issue_physical_card_api(self, request: IssuePhysicalCardRequestDict) -> Response:
        """
        Выпускает новую физическую карту.

        :param request: Данные для выпуска карты: userId и accountId.
        :return: Ответ сервера с данными выпущенной карты в формате Response.
        """
        return self.post("/api/v1/cards/issue-physical-card", json=request)
