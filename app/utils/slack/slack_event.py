import requests


def get_user_info(user_id, token):
    url = f'https://slack.com/api/users.info?user={user_id}'
    headers = {
        'Authorization': 'Bearer ' + token
    }

    res = requests.get(url=url, headers=headers)
    return res.json()


def is_mention(string_slack_event):
    if "'type': 'app_mention'" in string_slack_event:
        return True

    return False


def get_mention_message(slack_event):
    print(slack_event)
    return slack_event['event']['blocks'][0]['elements'][0]['elements'][1]['text']


def get_user_id_in_slack_event(slack_event):
    return slack_event['event']['user']


