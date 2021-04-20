import requests


def get_json(access_token):
    url = 'https://slack.com/api/conversations.list'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer ' + access_token
    }

    res = requests.get(url=url, headers=headers)
    return res.json()
