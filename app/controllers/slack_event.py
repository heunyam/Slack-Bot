import json
import os
import time

from flask_restful import Resource
from flask import request, make_response

from app.utils.slack.slack_event import get_mention_message, is_mention, get_user_info, get_user_id_in_slack_event
from app.utils.slack.message import post_message_to_channel
from app.service.answer import today_commit_state_message, commit_ranking_message


def get_answer(user_query, user_info):
    message = user_query
    if "커밋" in user_query:
        return today_commit_state_message(user_info)

    elif "랭킹" in user_query:
        return commit_ranking_message()

    return message


def event_handler(event_type, slack_event):
    channel = slack_event["event"]["channel"]
    string_slack_event = str(slack_event)

    if is_mention(string_slack_event):
        try:
            user_id = get_user_id_in_slack_event(slack_event)
            user_info = get_user_info(user_id, os.getenv('BOT_TOKEN'))
            user_query = get_mention_message(slack_event)
            answer = get_answer(user_query, user_info)
            post_message_to_channel(channel, answer, os.getenv('BOT_TOKEN'))
            return make_response("ok", 200)

        except IndexError:
            pass

    message = f"[{event_type}] cannot find event handler"

    return make_response(message, 200, {"X-Slack-No-Retry": 1})


class SlackEventAPI(Resource):
    def post(self):
        start = time.time()
        slack_event = json.loads(request.data)

        # 요청이 여러번 오는 것을 방지
        if 'X-Slack-Retry-Num' in str(request.headers):
            return make_response("Wait", 204, {"X-Slack-No-Retry": 1})

        # slack 연결 요청 처리
        if "challenge" in slack_event:
            return make_response(slack_event["challenge"], 200, {"content_type": "application/json"})

        # slack 이벤트 요청 처리
        if "event" in slack_event:
            event_type = slack_event.get("event").get("type")
            response = event_handler(event_type, slack_event)
            print(time.time() - start)
            return response

        # 처리하지 못하는 이벤트 처리
        return make_response("There are no slack request events", 404, {"X-Slack-No-Retry": 1})
