from datetime import datetime, timedelta
from github import Github


def get_today_commit_events(username, password):
    today = datetime.today()
    today_date = datetime(today.year, today.month, today.day)
    today_date_ko = today_date - timedelta(hours=9)

    client = Github(username, password)
    commit_events = []

    for event in client.get_user(username).get_events():
        if event.created_at > today_date_ko:
            if event.type in ['PushEvent', 'PullRequestEvent']:
                commit_events.append(event)

        else:
            break

    return commit_events
