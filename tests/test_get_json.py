from app import get_channels_data
from pytest_mock import MockerFixture


class MockResponse:
    def __init__(self, json_data):
        self.json_data = json_data

    def json(self):
        return self.json_data


def test_get_channels_data(mocker: MockerFixture) -> None:
    mock_json_data = {
        'ok': True
    }
    mocker.patch('src.get_channel_id.requests.get', return_value=MockResponse(mock_json_data))

    result = get_channels_data(BOT_OAUTH_ACCESS_TOKEN)
    assert result['ok'] is True


def test_get_channels_data_error(mocker: MockerFixture) -> None:
    mock_json_data = {
        'ok': False
    }
    mocker.patch('src.get_channel_id.requests.get', return_value=MockResponse(mock_json_data))

    result = get_channels_data(BOT_OAUTH_ACCESS_TOKEN)
    assert result['ok'] is False
