


def test_delete_v1_account_login(api):
    """
    Logout as current user
    :return:
    """

    headers = {
        'X-Dm-Auth-Token': 'IQJh+zgzF5DL+x6PqzFdX34Z+5M8mulgP5ABi3OaCOYk+Pog0kQxnAdhA2dxLo0691oj1mFZYBTrzsyQsf5gga4so7MV8ezvh0HN87pPF6HlQe3SPa6MRUJQtCzejYc0UKhD4Kk/sj0=',
        'X-Dm-Bb-Render-Mode': '',
        'Accept': 'text/plain'
    }

    response = api.login.delete_v1_account_login(
        headers=headers
    )
    assert response.status_code == 204