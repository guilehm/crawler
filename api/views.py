import json
import tempfile

from django.core.files import File
from django.shortcuts import redirect
from requests.exceptions import RequestException
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from core.models import DataFile
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


class FeedDetailSaveView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer,)

    def get(self, request, *args, **kwargs):
        feed_data = None
        try:
            feed_data = create_feed()
        except RequestException:
            status_code = HTTP_400_BAD_REQUEST
            return Response(
                data=feed_data,
                status=status_code,
            )

        with tempfile.TemporaryFile(mode='w+') as file:
            file.write(
                json.dumps(feed_data, indent=4, separators=(',', ': '), ensure_ascii=False)
            )
            file.seek(0)
            data_file = DataFile.objects.create(
                file=File(file, name='feed.json')
            )
        return redirect('core:feed-detail', feed_id=data_file.id)
