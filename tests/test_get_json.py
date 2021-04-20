from src.get_channel_id import get_json
from pytest_mock import MockerFixture
from config import BOT_OAUTH_ACCESS_TOKEN


def test_get_json(mocker: MockerFixture):
    mocker.patch('src.get_channel_id.request_get_to_slack')

    result = get_json(BOT_OAUTH_ACCESS_TOKEN)

    assert result['ok']
