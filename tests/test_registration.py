import allure
import pytest
import requests
import links
import data


class TestRegistration:

    @allure.title('Проверка создания уже созданной учетной записи пользователя и возвращения соответствующей ошибки в теле ответа')
    def test_create_same_user(self, user):
        payload = data.payload_login_exist_user()
        response = requests.post(links.EndPoints.EP_REGISTRATION, data=payload)
        assert response.status_code == 403 and response.json()['message'] == 'User already exists', f'response.status_code == {response.status_code} and response == {response.text}'

    @allure.title('Проверка создания новой учетной записи пользователя и возвращения соответствующего тела ответа')
    def test_create_new_user(self, remove_user):
        payload = data.payload_login_exist_user()
        response = requests.post(links.EndPoints.EP_REGISTRATION, data=payload)
        assert response.status_code == 200 and 'Bearer' in response.json()['accessToken'], f'response.status_code == {response.status_code} and response == {response.text}'

    @allure.title('Проверка создания новой учетной записи пользователя без одного из обязательных полей и возвращения соответствующей ошибки в теле ответа')
    @pytest.mark.parametrize('payload', data.payloads_without_1_field())
    def test_create_user_without_1_required_field(self, payload):
        response = requests.post(links.EndPoints.EP_REGISTRATION, data=payload)
        assert response.status_code == 403 and response.json()[
            'message'] == 'Email, password and name are required fields', f'response.status_code == {response.status_code} and response == {response.text}'

