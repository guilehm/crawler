from requests.exceptions import RequestException
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from utils import create_feed


class FeedDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    renderer_classes = (JSONRenderer,)

    def get(self, request, *args, **kwargs):
        status_code = HTTP_200_OK
        feed_data = None
        try:
            feed_data = create_feed()
        except RequestException:
            status_code = HTTP_400_BAD_REQUEST
        return Response(
            data=feed_data,
            status=status_code,
        )


class FeedDetailAllowAnyView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer,)

    def get(self, request, *args, **kwargs):
        status_code = HTTP_200_OK
        feed_data = None
        try:
            feed_data = create_feed()
        except RequestException:
            status_code = HTTP_400_BAD_REQUEST
        return Response(
            data=feed_data,
            status=status_code,
        )
