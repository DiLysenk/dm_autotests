import requests


def get_v1_account():
    """
    Get current user
    :return:
    """
    url = "http://5.63.153.31:5051/v1/account"

    headers = {
        'X-Dm-Auth-Token':'IQJh+zgzF5DL+x6PqzFdX34Z+5M8mulgP5ABi3OaCOYk+Pog0kQxnAdhA2dxLo0691oj1mFZYBTrzsyQsf5gga4so7MV8ezvh0HN87pPF6HlQe3SPa6MRUJQtCzejYc0UKhD4Kk/sj0=',
        'X-Dm-Bb-Render-Mode': '',
        'Accept': 'text/plain'
    }

    response = requests.request(
        method="GET",
        url=url,
        headers=headers,
    )
    return response
