from datetime import datetime
from typing import Optional

from pydantic import EmailStr, Field

from app.core.types import Model, PydanticObjectId


class UserProfile(Model):
    first_name: str = Field(...)
    last_name: str = Field(...)
    avatar: Optional[str] = Field(...)


class UserRegistrationInput(Model):
    profile: UserProfile = Field(...)
    username: EmailStr = Field(...)
    password: str = Field(...)
    repeat_password: str = Field(...)

    # @field_validator("password")
    # def validate_password_strength(cls, value):
    #     policy = PasswordPolicy()
    #     policy.minimum_length = 8
    #     policy.require_uppercase = True
    #     policy.require_lowercase = True
    #     policy.require_digits = True
    #     policy.require_special = True
    #
    #     result = policy.test(value)
    #     if not result:
    #         raise ValueError(
    #         f"Password does not meet requirements: {result}"
    #         )
    #     return value


class UserRegistrationOutput(Model):
    profile: UserProfile = Field(...)
    username: EmailStr = Field(...)


class User(Model):
    """Schema for user that which was set in jwt payload"""

    user_id: PydanticObjectId = Field(description="User id")
    permissions: list = Field(...)


class CurrentUserOutput(Model):
    user_id: PydanticObjectId = Field(description="User id", alias="_id")


class CompleteUserDatabaseOutput(Model):
    profile: UserProfile = Field(...)
    username: EmailStr = Field(...)
    permissions: list = Field(...)
    created_at: datetime = Field(...)
    updated_at: datetime = Field(...)


class CurrentUser(Model):
    user_id: PydanticObjectId = Field(description="User", alias="_id")
