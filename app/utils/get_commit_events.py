from datetime import datetime, timedelta
from github import Github

today = datetime.today()
today_date = datetime(today.year, today.month, today.day)
today_date_ko = today_date - timedelta(hours=9)
one_week_ago_ko = today_date_ko - timedelta(days=7)

username = 'heunyam'
password = 'sejun0702!'

client = Github(username, password)

commit_events = []

for event in client.get_user(username).get_events():
    if event.created_at > today_date_ko:
        if event.type in ['PushEvent', 'PullRequestEvent']:
            commit_events.append(event)

    else:
        break
