from src.get_channel_id import get_channels_data
from pytest_mock import MockerFixture
from config import BOT_OAUTH_ACCESS_TOKEN


def test_get_channels_data(mocker: MockerFixture):
    mocker.patch('src.get_channel_id.requests')

    result = get_channels_data(BOT_OAUTH_ACCESS_TOKEN)
    assert result['ok']
