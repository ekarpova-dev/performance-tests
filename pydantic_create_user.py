"""Pydantic-модели запроса и ответа для создания пользователя."""

from pydantic import BaseModel, EmailStr, Field


class UserSchema(BaseModel):
    """Данные пользователя, включая присвоенный сервером идентификатор."""

    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    phone_number: str = Field(alias="phoneNumber")


class CreateUserRequestSchema(BaseModel):
    """Обязательные данные для запроса POST /api/v1/users."""

    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    phone_number: str = Field(alias="phoneNumber")


class CreateUserResponseSchema(BaseModel):
    """Ответ API с данными созданного пользователя."""

    user: UserSchema
