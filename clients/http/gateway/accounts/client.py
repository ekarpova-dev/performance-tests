from typing import TypedDict

from httpx import QueryParams, Response

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


class CardDict(TypedDict):
    """Описывает структуру карты, вложенной в данные банковского счета."""

    id: str
    pin: str
    cvv: str
    type: str
    status: str
    accountId: str
    cardNumber: str
    cardHolder: str
    expiryDate: str
    paymentSystem: str


class AccountDict(TypedDict):
    """Описывает структуру банковского счета."""

    id: str
    type: str
    cards: list[CardDict]
    status: str
    balance: float


class GetAccountsQueryDict(TypedDict):
    """Описывает параметры запроса списка счетов пользователя."""

    userId: str


class GetAccountsResponseDict(TypedDict):
    """Описывает ответ со списком счетов пользователя."""

    accounts: list[AccountDict]


class OpenDepositAccountRequestDict(TypedDict):
    """Описывает запрос на открытие депозитного счета."""

    userId: str


class OpenDepositAccountResponseDict(TypedDict):
    """Описывает ответ на открытие депозитного счета."""

    account: AccountDict


class OpenSavingsAccountRequestDict(TypedDict):
    """Описывает запрос на открытие сберегательного счета."""

    userId: str


class OpenSavingsAccountResponseDict(TypedDict):
    """Описывает ответ на открытие сберегательного счета."""

    account: AccountDict


class OpenDebitCardAccountRequestDict(TypedDict):
    """Описывает запрос на открытие дебетового счета."""

    userId: str


class OpenDebitCardAccountResponseDict(TypedDict):
    """Описывает ответ на открытие дебетового счета."""

    account: AccountDict


class OpenCreditCardAccountRequestDict(TypedDict):
    """Описывает запрос на открытие кредитного счета."""

    userId: str


class OpenCreditCardAccountResponseDict(TypedDict):
    """Описывает ответ на открытие кредитного счета."""

    account: AccountDict


class AccountsGatewayHTTPClient(HTTPClient):
    """Клиент для взаимодействия с /api/v1/accounts сервиса http-gateway."""

    def get_accounts_api(self, query: GetAccountsQueryDict) -> Response:
        """
        Выполняет GET-запрос на получение счетов пользователя.

        :param query: Параметры запроса с идентификатором пользователя.
        :return: Ответ сервера в формате Response.
        """
        return self.get("/api/v1/accounts", params=QueryParams(**query))

    def open_deposit_account_api(self, request: OpenDepositAccountRequestDict) -> Response:
        """
        Выполняет POST-запрос на открытие депозитного счета.

        :param request: Данные пользователя для открытия счета.
        :return: Ответ сервера в формате Response.
        """
        return self.post("/api/v1/accounts/open-deposit-account", json=request)

    def open_savings_account_api(self, request: OpenSavingsAccountRequestDict) -> Response:
        """
        Выполняет POST-запрос на открытие сберегательного счета.

        :param request: Данные пользователя для открытия счета.
        :return: Ответ сервера в формате Response.
        """
        return self.post("/api/v1/accounts/open-savings-account", json=request)

    def open_debit_card_account_api(self, request: OpenDebitCardAccountRequestDict) -> Response:
        """
        Выполняет POST-запрос на открытие дебетового счета.

        :param request: Данные пользователя для открытия счета.
        :return: Ответ сервера в формате Response.
        """
        return self.post("/api/v1/accounts/open-debit-card-account", json=request)

    def open_credit_card_account_api(self, request: OpenCreditCardAccountRequestDict) -> Response:
        """
        Выполняет POST-запрос на открытие кредитного счета.

        :param request: Данные пользователя для открытия счета.
        :return: Ответ сервера в формате Response.
        """
        return self.post("/api/v1/accounts/open-credit-card-account", json=request)

    def get_accounts(self, user_id: str) -> GetAccountsResponseDict:
        """
        Получает счета пользователя в виде JSON-структуры.

        :param user_id: Идентификатор пользователя.
        :return: Словарь со списком счетов пользователя.
        """
        query = GetAccountsQueryDict(userId=user_id)
        response = self.get_accounts_api(query)
        return response.json()

    def open_deposit_account(self, user_id: str) -> OpenDepositAccountResponseDict:
        """
        Открывает депозитный счет и возвращает данные счета.

        :param user_id: Идентификатор пользователя.
        :return: Словарь с данными открытого счета.
        """
        request = OpenDepositAccountRequestDict(userId=user_id)
        response = self.open_deposit_account_api(request)
        return response.json()

    def open_savings_account(self, user_id: str) -> OpenSavingsAccountResponseDict:
        """
        Открывает сберегательный счет и возвращает данные счета.

        :param user_id: Идентификатор пользователя.
        :return: Словарь с данными открытого счета.
        """
        request = OpenSavingsAccountRequestDict(userId=user_id)
        response = self.open_savings_account_api(request)
        return response.json()

    def open_debit_card_account(self, user_id: str) -> OpenDebitCardAccountResponseDict:
        """
        Открывает дебетовый счет и возвращает данные счета.

        :param user_id: Идентификатор пользователя.
        :return: Словарь с данными открытого счета.
        """
        request = OpenDebitCardAccountRequestDict(userId=user_id)
        response = self.open_debit_card_account_api(request)
        return response.json()

    def open_credit_card_account(self, user_id: str) -> OpenCreditCardAccountResponseDict:
        """
        Открывает кредитный счет и возвращает данные счета.

        :param user_id: Идентификатор пользователя.
        :return: Словарь с данными открытого счета.
        """
        request = OpenCreditCardAccountRequestDict(userId=user_id)
        response = self.open_credit_card_account_api(request)
        return response.json()


def build_accounts_gateway_http_client() -> AccountsGatewayHTTPClient:
    """
    Создает настроенный клиент для работы со счетами.

    :return: Готовый экземпляр AccountsGatewayHTTPClient.
    """
    return AccountsGatewayHTTPClient(client=build_gateway_http_client())
