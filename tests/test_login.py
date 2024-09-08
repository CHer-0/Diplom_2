import allure
import pytest
import requests
import links
import data


class TestLogin:

    @allure.title('Проверка логина с существующей учетной записью пользователя и возвращения соответствующего тела ответа')
    def test_login_exist_user(self, user):
        payload = data.payload_login_exist_user()
        response = requests.post(links.EndPoints.EP_LOGIN, data=payload)
        assert response.status_code == 200 and 'Bearer' in response.json()['accessToken'] and response.json()['refreshToken'], f'response.status_code == {response.status_code} and response == {response.text}'

    @allure.title('Проверка логина с учетной записью пользователя с неверным логином/паролем по очереди и возвращения соответствующей ошибки в теле ответа')
    @pytest.mark.parametrize('payload', data.payloads_wrong_1_field())
    def test_create_user_without_1_required_field(self, payload):
        response = requests.post(links.EndPoints.EP_LOGIN, data=payload)
        assert response.status_code == 401 and response.json()[
            'message'] == 'email or password are incorrect', f'response.status_code == {response.status_code} and response == {response.text}'

