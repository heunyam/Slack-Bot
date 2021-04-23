import requests


def get_channels_data(token) -> dict:
    url = 'https://slack.com/api/conversations.list'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer ' + token
    }

    res = requests.get(url=url, headers=headers)
    return res.json()


def get_channels(token) -> list:
    data = get_channels_data(token)

    return data.get('channels')


def get_channel_id(channel_name, token) -> str:
    channels = get_channels(token)

    for channel in channels:
        if channel['name'] == channel_name:
            return channel['id']
