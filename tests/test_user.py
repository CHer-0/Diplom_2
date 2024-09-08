import allure
import pytest
import requests
import links
import data


class TestUser:

    @allure.title(
        'Проверка изменения логина/пароля по очереди учетной записи авторизованного пользователя и возвращения соответствующего тела ответа')
    @pytest.mark.parametrize('payload', data.payload_changed_user())
    def test_change_authorized_user(self, payload, user):
        response = requests.patch(links.EndPoints.EP_USER, headers={'authorization': f'{user}'}, data=payload)
        assert response.status_code == 200 and response.json()['user']['email'] == payload['email'] and \
               response.json()['user']['name'] == payload[
                   'name'], f'response.status_code == {response.status_code} and response == {response.text}'

    @allure.title('Проверка изменения логина/пароля по очереди учетной записи неавторизованного пользователя и возвращения соответствующей ошибки в теле ответа')
    @pytest.mark.parametrize('payload', data.payload_changed_user())
    def test_change_unauthorized_user(self, user, payload):
        response = requests.patch(links.EndPoints.EP_USER, data=payload)
        assert response.status_code == 401 and response.json()['message'] == 'You should be authorised', f'response.status_code == {response.status_code} and response == {response.text}'

