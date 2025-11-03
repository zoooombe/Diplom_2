import pytest
import requests
import generators
from data import Url

@pytest.fixture
def create_uniq_user():
    email = generators.email_generator()
    password = generators.password_generator()
    name = generators.name_generator()
    create_user_body = {"email": email, "password": password, "name": name}
    login_user_body = {"email": email, "password": password}
    user_login = requests.post(f'{Url.LOGIN_USER}', json=login_user_body)
    yield [create_user_body, login_user_body]
    requests.delete(f'{Url.DELETE_USER}{user_login.json().get("accessToken")}')

@pytest.fixture
def create_duplicate_user():
    email = generators.email_generator()
    password = generators.password_generator()
    name = generators.name_generator()
    create_user_body = {"email": email, "password": password, "name": name}
    requests.post(Url.CREATE_USER, json=create_user_body)
    login_user_body = {"email": email, "password": password}
    user_login = requests.post(f'{Url.LOGIN_USER}', json=login_user_body)
    yield create_user_body
    requests.delete(f'{Url.DELETE_USER}{user_login.json().get("accessToken")}')