from datetime import datetime, timedelta
from github import Github
import os


def get_today_commit_events(user_id):
    today = datetime.today()
    today_date = datetime(today.year, today.month, today.day)
    today_date_ko = today_date - timedelta(hours=9)

    client = Github(login_or_token=os.getenv('GITHUB_TOKEN'))
    commit_events = []
    events = client.get_user(user_id).get_events()

    for event in events:
        if event.created_at > today_date_ko:
            if event.type in ['PushEvent', 'PullRequestEvent']:
                commit_events.append(event)

        else:
            break

    return commit_events
