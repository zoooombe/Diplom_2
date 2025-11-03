import allure
import requests
import api_requests
import data


class TestCreateOrder:

    @allure.title('Тест на создание заказа с авторизацией, ручка: /api/orders')
    def test_create_order_with_login_user(self, create_duplicate_user):
        api_requests.login_user(create_duplicate_user)
        response = api_requests.create_order_with_login(create_duplicate_user)
        response_body = response.json()

        assert response.status_code == 200
        assert response_body['success'] is True
        assert 'name' in response_body.keys()
        assert 'owner' in response_body['order'].keys()

    @allure.title('Тест на создание заказа без авторизации, ручка: /api/orders')
    def test_create_order_without_login_user(self):
        payload = data.OrderIngredients.INGREDIENTS
        response = requests.post(f'{data.Url.CREATE_ORDER}', json=payload)
        response_body = response.json()

        assert response.status_code == 200
        assert response_body['success'] is True
        assert 'name' in response_body.keys()
        assert 'number' in response_body['order'].keys()

    @allure.title('Тест на создание заказа с ингредиентами, ручка: /api/orders')
    def test_create_order_with_ingredient(self):
        payload = data.OrderIngredients.INGREDIENTS
        response = requests.post(f'{data.Url.CREATE_ORDER}', json=payload)
        response_body = response.json()

        assert response.status_code == 200
        assert response_body['success'] is True

    @allure.title('Тест на создание заказа без ингредиентов, ручка: /api/orders')
    def test_create_order_without_ingredient(self):
        payload = data.OrderIngredients.NO_INGREDIENTS
        response = requests.post(f'{data.Url.CREATE_ORDER}', json=payload)
        response_body = response.json()

        assert response.status_code == 400
        assert response_body == data.ResponseBody.INGREDIENTS_NOT_TRANSFER

    @allure.title('Тест на создание заказа с неверным хешем ингредиентов, ручка: /api/orders')
    def test_create_order_with_bad_hash(self):
        payload = data.OrderIngredients.BAD_HASH_INGREDIENT
        response = requests.post(f'{data.Url.CREATE_ORDER}', json=payload)

        assert response.status_code == 500
