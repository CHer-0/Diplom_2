class Urls:
    URL_MAIN = 'https://stellarburgers.nomoreparties.site'


class EndPoints:
    EP_ORDER = Urls.URL_MAIN + '/api/orders'
    EP_ORDERS = EP_ORDER + '/all'
    EP_REGISTRATION = Urls.URL_MAIN + '/api/auth/register'
    EP_LOGIN = Urls.URL_MAIN + '/api/auth/login'
    EP_USER = Urls.URL_MAIN + '/api/auth/user'