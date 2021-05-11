from rest_framework.views import Response, APIView
import os


class HelloAPI(APIView):
    def get(self, *args, **kwargs):
        return Response({
            'hello': os.environ['SLACK_BOT_ACCESS_TOKEN']
        })


class PingAPI(APIView):
    def get(self, *args, **kwargs):
        return Response({
            'ping': 'pong1'
        })
