import string
from random import choice

import allure
import requests
from pydantic import BaseModel


def validate_request_json(json: dict | BaseModel):
    if isinstance(json, dict):
        return json
    return json.model_dump(by_alias=True, exclude_none=True)


def validate_status_code_func(response: requests.Response, status_code: int):
    with allure.step('Проверка валидации и статус кода'):
        assert (
                response.status_code == status_code
        ), f'Статус-код ответа должен быть равен {status_code},но он равен {response.status_code}'


def generate_random_string(length: int) -> str:
    """Метод для генерации рандомной строки заданной длины"""
    try:
        letters = string.ascii_lowercase
        return ''.join(choice(letters) for _ in range(length))
    except TypeError as e:
        msg = 'need integer'
        raise AssertionError(msg) from e


def validate_status_code(status):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            response = func(*args, **kwargs)
            with allure.step('Статус код'):
                assert response.status_code == status, AssertionError(
                    f'Ожидаемый статус-код ответа = {status}, фактический {response.status_code}\n'
                    f'response={response.json}',
                )
            return response

        return wrapper

    return actual_decorator
