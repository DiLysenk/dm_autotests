import structlog

from dm_api_account.apis.models.regisration_user_model import RegistrationModel

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account(api, mailhog):
    response = api.account.post_v1_account(json=RegistrationModel())
    assert response.status_code == 201,\
        f'expected 201 but equals {response.status_code}, \n{response.json(indent=2)}'
