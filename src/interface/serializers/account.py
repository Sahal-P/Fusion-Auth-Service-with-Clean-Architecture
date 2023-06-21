from marshmallow import Schema, fields, validate, validates, validates_schema, EXCLUDE
from marshmallow.decorators import post_load
from marshmallow.exceptions import ValidationError
import re
from src.domain.services.account import (
    decode_access_token,
    generate_password_hash,
    decode_refresh_token,
)
from src.domain.exceptions import InvalidToken


class UserSerializer(Schema):
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    username = fields.String(required=True)
    phone = fields.String(required=True)
    email = fields.Email(required=True)
    is_active = fields.Boolean(required=True)
    last_login = fields.DateTime(required=True)
    date_joined = fields.DateTime(required=True)

    def load(self, data: dict) -> dict:
        try:
            data = super().load(data)
        except ValidationError as err:
            data = {"errors": err.messages}
        return data


class NewUserSerializer(Schema):
    email = fields.Email(required=True)

    class Meta:
        unknown = EXCLUDE


class UserLoginSerializer(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True)

    def load(self, data: dict) -> dict:
        try:
            data = super().load(data)
        except ValidationError as err:
            data = {"errors": err.messages}
        return data

    @post_load
    def make_password_hash(self, data: dict, **kwargs) -> dict:
        data["password"] = generate_password_hash(data["password"])
        return data


class TokenSerializer(Schema):
    token = fields.String(required=True)

    def load(self, data: dict) -> dict:
        try:
            data = super().load(data)
        except ValidationError as err:
            data = {"errors": err.messages}
        return data

    @post_load
    def make_payload(self, data: dict, **kwargs) -> dict:
        try:
            data["payload"] = decode_access_token(data["token"])

        except InvalidToken as err:
            data = {"errors": err.message}
        return data


class RefreshTokenSerializer(Schema):
    token = fields.String(required=True)

    def load(self, data: str) -> str:
        try:
            data = super().load(data)
        except ValidationError as err:
            data = {"errors": err.messages}
        return data

    @post_load
    def make_payload(self, data: dict, **kwargs) -> dict:
        try:
            data["payload"] = decode_refresh_token(data["token"])

        except InvalidToken as err:
            data = {"errors": err.message}
        return data


class UserRegisterSerializer(Schema):
    name = fields.String(required=True, validate=validate.Length(min=3, max=15))
    surname = fields.String(validate=validate.Length(min=3, max=15))
    username = fields.String(required=True, validate=validate.Length(min=3, max=10))
    email = fields.String(required=True, validate=validate.Length(min=5, max=50))
    phone = fields.String(required=True, validate=validate.Length(min=10, max=15))
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(min=8, max=20))
    password_confirm = fields.String(
        required=True, validate=validate.Length(min=8, max=20)
    )

    @staticmethod
    def _validate_password(value: str):
        if not any(char.isalpha() for char in value):
            raise ValidationError("Password should have at least two letters.")
        if not any(char.isdigit() for char in value):
            raise ValidationError("Password should have at least one numeral.")
        if not any(char.islower() for char in value):
            raise ValidationError("Password should have at least one lowercase letter.")
        if not any(char.isupper() for char in value):
            raise ValidationError(
                "Password should have at least one uppercase letters."
            )
        if re.search("[_$@#%]", value) is None:
            raise ValidationError(
                "Password should have at least one special charecter: _$@ #%"
            )

    @validates("password")
    def validate_password(self, value: str):
        self._validate_password(value)

    @validates_schema
    def check_password(self, data: dict, **kwargs):
        if data["password"] != data["password_confirm"]:
            raise ValidationError("Password Fields do not match")

    def load(self, data: dict) -> dict:
        try:
            data = super().load(data)
        except ValidationError as err:
            data = {"errors": err.messages}
        return data

    @post_load
    def make_password_hash(self, data: dict, **kwargs) -> dict:
        data.pop("password_confirm")
        data["password"] = generate_password_hash(data["password"])
        return data


class UserCreatedQueueSerializer(Schema):
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    surname = fields.String()
    username = fields.String(required=True)
    phone = fields.String(required=True)
    email = fields.Email(required=True)

    def load(self, data: dict) -> dict:
        try:
            data = super().load(data)
        except ValidationError as err:
            data = {"errors": err.messages}
        return data
