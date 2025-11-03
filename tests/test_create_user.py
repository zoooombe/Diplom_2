import allure
import pytest
import requests
import data

class TestUserCreation:
    @allure.title('Тест на создание нового пользователя, ручка: /api/auth/register')
    def test_create_user (self, create_uniq_user):
        response = requests.post(f'{data.Url.CREATE_USER}', json=create_uniq_user[0])
        response_body = response.json()
        assert response_body['success'] is True
        assert response_body['user']['email'] == create_uniq_user[0]['email']
        assert response_body['user']['name'] == create_uniq_user[0]['name']
        assert 'accessToken' in response_body
        assert 'refreshToken' in response_body
        assert response.status_code == 200

    @allure.title('Тест попытку на создать пользователя, который уже зарегистрирован, ручка: /api/auth/register')
    def test_create_duplicate_user (self, create_duplicate_user):
        response = requests.post(f'{data.Url.CREATE_USER}', json=create_duplicate_user)
        response_body = response.json()
        assert response_body == data.ResponseBody.USER_EXIST
        assert response.status_code == 403

    @allure.title('Тест на попытку создать пользователя и не заполнить одно из обязательных полей, ручка: /api/auth/register')
    @pytest.mark.parametrize('registration_data', data.MissingDataForUser.user_creation_with_missing_field)
    def test_create_user_with_missing_fields (self, registration_data):
        response = requests.post(f'{data.Url.CREATE_USER}', json=registration_data)
        assert response.json() == data.ResponseBody.USER_FIELD_MISSING
        assert response.status_code == 403
