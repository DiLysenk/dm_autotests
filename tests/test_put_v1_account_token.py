import structlog

from dm_api_account.apis.models.activate_registered_user_model import ResponseActivated

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_token(api, mailhog, create_user):
    token = mailhog.get_token_from_last_email()
    response = api.account.put_v1_account_token(token=token)
    assert response.status_code == 200, f'expected 200 but equals {response.status_code}'
