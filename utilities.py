import string
from random import choice

import allure
import requests
from pydantic import BaseModel
from string import ascii_letters, digits
import random


def validate_request_json(json: dict | BaseModel):
    if isinstance(json, dict):
        return json
    return json.model_dump(by_alias=True, exclude_none=True)


def validate_status_code(response: requests.Response, status_code: int):
    with allure.step('Проверка валидации и статус кода'):
        assert response.status_code == status_code, \
            (f'Статус-код ответа должен быть равен {status_code},\n'
             f'но он равен {response.status_code},\n'
             f' {response.json()}')


def generate_random_string(length: int) -> str:
    """Метод для генерации рандомной строки заданной длины"""
    try:
        letters = string.ascii_lowercase
        return ''.join(choice(letters) for _ in range(length))
    except TypeError as e:
        msg = 'need integer'
        raise AssertionError(msg) from e


def reiterate(fn):
    def wrapper(*args, **kwargs):
        for i in range(5):
            response = fn(*args, **kwargs)
            emails = response.json()['items']
            if len(emails) < 5:
                print(f'attempt{i}')
                continue
            else:
                return response

    return wrapper


def random_string(count_of_symbols=8):
    symbols = ascii_letters + digits
    string = ''
    for _ in range(count_of_symbols):
        string += random.choice(symbols)
    return string
