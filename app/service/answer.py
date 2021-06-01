from app.utils.github import get_today_commit_events
import os

from app.models.user import User


def today_commit_state_message(user_info):
    username = user_info['user']['real_name']
    user_account = User.get_user_account(username=username)

    if user_account:
        commit_events = get_today_commit_events(user_account.id)
        message = f'{username}님의 오늘 커밋은 {len(commit_events)} 개 입니다.'
        if len(commit_events) < 1:
            message += f"\n아직도 커밋을 하지 않았네요. 오늘이 가기 전에 커밋을 합시다!"
    else:
        message = '로그인을 먼저 해주세요!\n'
        message += f'{os.getenv("BASE_URL")}/page/login'

    return message


def commit_ranking_message():
    users = User.get_users()
    ranking = {}
    message = ''

    for i, user in enumerate(users):
        user_today_commit = get_today_commit_events(user.id)

        ranking[user.name] = len(user_today_commit)

    sorted_ranking = dict(sorted(ranking.items(), key=lambda x: x[1], reverse=True))

    for user in sorted_ranking:
        message += f"{user} : {ranking[user]}\n"

    message += f"1등은 {list(sorted_ranking.keys())[0]} 입니다!"

    return message
