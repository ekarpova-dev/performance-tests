import uuid
from datetime import date

from pydantic import BaseModel, Field, HttpUrl, EmailStr, ValidationError

# Добавили модель UserSchema
class UserSchema(BaseModel):
    id: str
    email: EmailStr  # Используем EmailStr вместо str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    phone_number: str = Field(alias="phoneNumber")


# Добавили модель UserSchema
class CreateUserRequestSchema(BaseModel):
    email: EmailStr  # Используем EmailStr вместо str
    last_name: str
    first_name: str
    middle_name: str
    phone_number: str

# Добавили модель UserSchema
class CreateUserResponseSchema(BaseModel):
    id: str
    email: EmailStr  # Используем EmailStr вместо str
    last_name: str
    first_name: str
    middle_name: str
    phone_number: str
