import json
from flask_restful import Resource
from flask import request, make_response
from config import BOT_TOKEN

from app.utils.slack.slack_event import get_mention_message, is_mention, get_user_info, get_user_id_in_slack_event
from app.utils.github import get_today_commit_events
from app.utils.slack.message import post_message_to_channel


def get_answer(user_query, user_info):
    if "커밋" in user_query:
        print(user_info)
        username = user_info['user']['real_name']
        commit_events = get_today_commit_events('heunyam', 'sejun0702!')
        message = f'{username}님의 오늘 커밋은 {len(commit_events)} 개 입니다.'
        if len(commit_events) < 10:
            message += f"\n{len(commit_events)}개? 개빠졌네 {10 - len(commit_events)} 커밋만 더 하자"

        return message

    else:
        return user_query


def event_handler(event_type, slack_event):
    channel = slack_event["event"]["channel"]
    string_slack_event = str(slack_event)

    if is_mention(string_slack_event):
        try:
            user_id = get_user_id_in_slack_event(slack_event)
            user_info = get_user_info(user_id, BOT_TOKEN)
            user_query = get_mention_message(slack_event)
            answer = get_answer(user_query, user_info)
            post_message_to_channel(channel, answer, BOT_TOKEN)
            return make_response("ok", 200)

        except IndexError:
            pass

    message = f"[{event_type}] cannot find event handler"

    return make_response(message, 200, {"X-Slack-No-Retry": 1})


class HelloAPI(Resource):
    def get(self):
        return {
            'message': 'hello world'
        }

    def post(self):
        slack_event = json.loads(request.data)

        if "challenge" in slack_event:
            return make_response(slack_event["challenge"], 200, {"content_type": "application/json"})

        if "event" in slack_event:
            event_type = slack_event["event"]["type"]

            return event_handler(event_type, slack_event)

        return make_response("There are no slack request events", 404, {"X-Slack-No-Retry": 1})
