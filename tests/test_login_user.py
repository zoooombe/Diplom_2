import allure
import requests
import data

class TestUserLogin:
    @allure.title('Тест на вход под существующим пользователем, ручка: /api/auth/login')
    def test_login_current_user(self, create_duplicate_user):
        response = requests.post(f'{data.Url.LOGIN_USER}', json=create_duplicate_user)
        response_body = response.json()
        assert response_body['success'] is True
        assert 'accessToken' in response_body
        assert 'refreshToken' in response_body
        assert response_body['user']['email'] == create_duplicate_user['email']
        assert response_body['user']['name'] == create_duplicate_user['name']
        assert response.status_code == 200

    @allure.title('Тест на попытку входа с неверным логином и паролем, ручка: /api/auth/register, ручка: /api/auth/login')
    def test_login_user_with_wrong_login_and_password(self):
        payload = data.WrongDataForLoginUser.wrong_data_for_login_user
        response = requests.post(f'{data.Url.LOGIN_USER}', json=payload)
        assert response.json() == data.ResponseBody.USER_UNAUTHORIZED
        assert response.status_code == 401