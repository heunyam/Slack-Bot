from config import BOT_OAUTH_ACCESS_TOKEN
from src.get_channel_id import get_channel_id
from src.post_message import post_message_to_channel


if __name__ == '__main__':
    channel_name = "bot"
    channel_id = get_channel_id(channel_name=channel_name, token=BOT_OAUTH_ACCESS_TOKEN)

    post_message_to_channel(channel_name, "test", token=BOT_OAUTH_ACCESS_TOKEN)
