import json
from flask_restful import Resource
from flask import request, make_response
from config import BOT_TOKEN
from app.utils.post_message import post_message_to_channel
from app.utils.get_commit_events import get_today_commit_events


def get_answer(user_query):
    if "커밋" in user_query:
        commit_events = get_today_commit_events('heunyam', 'sejun0702!')
        message = f'오늘 커밋은 {len(commit_events)} 개 입니다.'
        if len(commit_events) < 10:
            message += f"\n{len(commit_events)}개? 개빠졌네 {10 - len(commit_events)} 커밋만 더 하자"

        return message

    else:
        return user_query


def get_mention_message(slack_event):
    return slack_event['event']['blocks'][0]['elements'][0]['elements'][1]['text']


def is_mention(string_slack_event):
    if "'type': 'app_mention'" in string_slack_event:
        return True

    return False


def event_handler(event_type, slack_event):
    channel = slack_event["event"]["channel"]
    string_slack_event = str(slack_event)

    if is_mention(string_slack_event):
        try:
            user_query = get_mention_message(slack_event)
            answer = get_answer(user_query)
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
