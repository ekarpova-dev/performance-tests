import time
from typing import TypedDict

from httpx import Response

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


class UserDict(TypedDict):
    """Описывает структуру пользователя."""

    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str
    phoneNumber: str


class CreateUserRequestDict(TypedDict):
    """Описывает тело запроса на создание пользователя."""

    email: str
    lastName: str
    firstName: str
    middleName: str
    phoneNumber: str


class CreateUserResponseDict(TypedDict):
    """Описывает ответ на создание пользователя."""

    user: UserDict


class UsersGatewayHTTPClient(HTTPClient):
    """Клиент для взаимодействия с /api/v1/users сервиса http-gateway."""

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Выполняет POST-запрос на создание пользователя.

        :param request: Данные создаваемого пользователя.
        :return: Ответ сервера в формате Response.
        """
        return self.post("/api/v1/users", json=request)

    def create_user(self) -> CreateUserResponseDict:
        """
        Создает пользователя с уникальным адресом электронной почты.

        :return: Словарь с данными созданного пользователя.
        """
        request = CreateUserRequestDict(
            email=f"user.{time.time()}@example.com",
            lastName="string",
            firstName="string",
            middleName="string",
            phoneNumber="string",
        )
        response = self.create_user_api(request)
        return response.json()


def build_users_gateway_http_client() -> UsersGatewayHTTPClient:
    """
    Создает настроенный клиент для работы с пользователями.

    :return: Готовый экземпляр UsersGatewayHTTPClient.
    """
    return UsersGatewayHTTPClient(client=build_gateway_http_client())
