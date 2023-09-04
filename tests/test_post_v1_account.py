import structlog

from dm_api_account.apis.models.register_new_user import Registration

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account(api):
    api.account.post_v1_account(json=Registration())

