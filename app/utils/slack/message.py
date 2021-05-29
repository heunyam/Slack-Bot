import requests


def post_message_to_channel(channel_id, message, token):
    url = 'https://slack.com/api/chat.postMessage'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer ' + token,
        'reply_broadcast': 'True'
    }
    data = {
        'channel': channel_id,
        'text': message
    }

    res = requests.post(url=url, headers=headers, data=data)
    return res.json()
