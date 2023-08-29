import requests

from dm_api_account.apis.models.logout_from_every_device_model import ResponseLogoutEveryDevice


def test_delete_v1_account_login_all(api):
    """
    Logout from every device
    :return:
    """

    headers = {
        'X-Dm-Auth-Token': 'IQJh+zgzF5DL+x6PqzFdX34Z+5M8mulgP5ABi3OaCOYk+Pog0kQxnAdhA2dxLo0691oj1mFZYBTrzsyQsf5gga4so7MV8ezvh0HN87pPF6HlQe3SPa6MRUJQtCzejYc0UKhD4Kk/sj0=',
        'X-Dm-Bb-Render-Mode': '',
        'Accept': 'text/plain'
    }

    response = api.login.delete_v1_account_login_all(
        headers=headers,
    )
    assert response.status_code == 204