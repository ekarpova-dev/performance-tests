import time

import httpx

# Данные для создания пользователя
create_user_payload = {
    "email": f"user.{time.time()}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}

# Выполняем запрос на создание пользователя
create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()

# Выводим полученные данные пользователя
print("Create user response:", create_user_response_data)
print("Status Code:", create_user_response.status_code)
# Данные для создания депозита
create_deposit_payload = {
    "userId": create_user_response_data["user"]["id"]
}
# Выполняем запрос на создание депозита по ID
create_deposit_response = httpx.post("http://localhost:8003/api/v1/accounts/open-deposit-account",
                                     json=create_deposit_payload)

create_deposit_response_data = create_deposit_response.json()

# Выводим полученные данные
print("Create deposit response:", create_deposit_response_data)
print("Status Code:", create_deposit_response.status_code)
