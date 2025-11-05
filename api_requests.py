import allure
import requests
import data
from tests.conftest import create_duplicate_user

@allure.step("Логин пользователя")
def login_user(create_duplicate_user):
    response = requests.post(data.Url.LOGIN_USER, json=create_duplicate_user)
    return response

@allure.step("Получение access токена для пользователя")
def get_access_token(create_duplicate_user):
    login_user_body = create_duplicate_user
    response = requests.post(data.Url.LOGIN_USER, json=login_user_body)
    token = response.json().get("accessToken")
    return token

@allure.step("Создание заказа с авторизацией")
def create_order_with_login(create_duplicate_user):
    token = get_access_token(create_duplicate_user)
    headers = {"Authorization": f"{token}"}
    payload = data.OrderIngredients.INGREDIENTS
    return requests.post(data.Url.CREATE_ORDER, json=payload, headers=headers)
