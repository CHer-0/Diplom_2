import allure
import pytest
import links
import data
import requests


@allure.step('Создаем новую учетную запись курьера, возвращаем ее ID и по окончании теста ее удаляем')
@pytest.fixture()
def user():
    payload = data.payload_login_exist_user()
    requests.post(links.EndPoints.EP_REGISTRATION, data=payload)
    user = requests.post(links.EndPoints.EP_LOGIN, data=payload).json()['accessToken']

    yield user
    #user = requests.post(links.EndPoints.EP_LOGIN, data=payload).json()['accessToken']
    requests.delete(links.EndPoints.EP_USER, headers={'authorization': f'{user}'})


@pytest.fixture()
def remove_user():
    payload = data.payload_login_exist_user()
    try:
        user_data = requests.post(links.EndPoints.EP_LOGIN, data=payload).json()['accessToken']
        requests.delete(links.EndPoints.EP_USER, headers={'authorization': f'{user_data}'})
    except KeyError:
        pass
