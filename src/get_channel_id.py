import requests


def get_channels_data(access_token) -> dict:
    url = 'https://slack.com/api/conversations.list'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer ' + access_token
    }

    res = requests.get(url=url, headers=headers)
    return res.json()
