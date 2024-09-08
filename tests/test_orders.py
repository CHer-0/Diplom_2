import allure
import requests
import links
import data


class TestOrders:

    @allure.title('Проверка создания заказа без авторизации с ингредиентами и возвращения соответствующего тела ответа')
    def test_make_valid_order_no_login(self):
        payload = data.payload_ingredients_to_order()
        response = requests.post(links.EndPoints.EP_ORDER, data=payload)
        assert response.status_code == 200 and response.json()[
            'name'] == data.burger_name(), f'response.status_code == {response.status_code} and response == {response.text}'

    @allure.title('Проверка создания заказа с авторизацией с ингредиентами и возвращения соответствующего тела ответа')
    def test_make_valid_order_login(self, user):
        payload = data.payload_ingredients_to_order()
        response = requests.post(links.EndPoints.EP_ORDER, headers={'authorization': f'{user}'}, data=payload)
        assert response.status_code == 200 and response.json()[
            'name'] == data.burger_name(), f'response.status_code == {response.status_code} and response == {response.text}'

    @allure.title('Проверка создания заказа с авторизацией без ингредиентов и возвращения соответствующего тела ответа')
    def test_make_order_login_no_ingredients(self, user):
        payload = {}
        response = requests.post(links.EndPoints.EP_ORDER, headers={'authorization': f'{user}'}, data=payload)
        assert response.status_code == 400 and response.json()[
            'message'] == "Ingredient ids must be provided", f'response.status_code == {response.status_code} and response == {response.text}'

    @allure.title('Проверка создания заказа без авторизации и без ингредиентов и возвращения соответствующего тела ответа')
    def test_make_order_no_login_no_ingredients(self):
        payload = {}
        response = requests.post(links.EndPoints.EP_ORDER, data=payload)
        assert response.status_code == 400 and response.json()[
            'message'] == "Ingredient ids must be provided", f'response.status_code == {response.status_code} and response == {response.text}'

    @allure.title('Проверка создания заказа без авторизации с неверным хешем ингредиентов и возвращения соответствующего тела ответа')
    def test_make_order_wrong_ingredients(self):
        payload = data.payload_wrong_ingredients_to_order()
        response = requests.post(links.EndPoints.EP_ORDER, data=payload)
        assert response.status_code == 400 and response.json()[
            'message'] == "One or more ids provided are incorrect", f'response.status_code == {response.status_code} and response == {response.text}'

    @allure.title('Проверка получения списка заказов пользователя с авторизацией и возвращения соответствующего тела ответа')
    def test_get_users_orders_login(self, user):
        response = requests.get(links.EndPoints.EP_ORDER, headers={'authorization': f'{user}'})
        assert response.status_code == 200 and type(response.json()[
                                                        "orders"] == list), f'response.status_code == {response.status_code} and response == {response.text}'

    @allure.title(
        'Проверка получения списка заказов без авторизации и возвращения соответствующего сообщения об ошибке в теле ответа')
    def test_get_users_orders_no_login(self):
        response = requests.get(links.EndPoints.EP_ORDER)
        assert response.status_code == 401 and type(response.json()[
                                                        "message"] == "You should be authorised"), f'response.status_code == {response.status_code} and response == {response.text}'
