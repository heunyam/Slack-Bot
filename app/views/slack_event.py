import json
from flask_restful import Resource
from flask import request, make_response
from config import BOT_TOKEN
from slacker import Slacker
from app.utils.post_message import post_message_to_channel


def get_answer(user_query):
    return user_query


def event_handler(event_type, slack_event):
    slack = Slacker(BOT_TOKEN)

    channel = slack_event["event"]["channel"]
    string_slack_event = str(slack_event)

    if string_slack_event.find("{'type': 'user', 'user_id': ") != -1:  # 멘션으로 호출
        try:
            user_query = slack_event['event']['blocks'][0]['elements'][0]['elements'][1]['text']
            answer = get_answer(user_query)
            post_message_to_channel(channel, answer, BOT_TOKEN)
            return make_response("ok", 200)

        except IndexError:
            pass

    message = "[%s] cannot find event handler" % event_type

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
