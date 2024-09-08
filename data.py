import allure


@allure.step("подставим учетные данные нового тестового пользователя")
def payload_login_exist_user():
    return {
        "email": "vivrus@ya.ru",
        "password": "password",
        "name": "Username"
    }


def payloads_without_1_field():
    payload_1 = {
        "email": "",
        "password": "password",
        "name": "Username"
    }
    payload_2 = {
        "email": "vivrus@ya.ru",
        "password": "",
        "name": "Username"
    }
    payload_3 = {
        "email": "vivrus@ya.ru",
        "password": "password",
        "name": ""
    }
    return [payload_1, payload_2, payload_3]


def payloads_wrong_1_field():
    payload_1 = {
        "email": "vivrus@ya.ru",
        "password": "wrong",
        "name": "Username"
    }
    payload_2 = {
        "email": "wrong",
        "password": "password",
        "name": "Username"
    }
    return [payload_1, payload_2]


def payload_changed_user():
    return [{"email": "vivrus@yandex.com", "name": "Username"},
            {"email": "vivrus@ya.ru", "name": "New_Username"}]


def payload_ingredients_to_order():
    return {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]}


def burger_name():
    return "Бессмертный флюоресцентный бургер"


def payload_wrong_ingredients_to_order():
    return {"ingredients": ["61c0c5a71d1f82001bdaaa60", "61c0c5a71d1f82001bdaaa60"]}
