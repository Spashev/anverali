import json

from rest_framework import generics, status
from rest_framework.response import Response

from webhook.models import NamesMan, NamesWoman
from webhook.serializers import QuerySerializer
from webhook.services import get_names, send_data_to_back_url


class ContactViewSet(generics.GenericAPIView):
    serializer_class = QuerySerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = get_names(serializer.validated_data)

        if len(data) == 0:
            return Response(data={'message': 'Contact not found'}, status=status.HTTP_404_NOT_FOUND)

        response = send_data_to_back_url(
            data=data.get('contacts'),
            url=data.get('back_url')
        )

        if response.status_code == status.HTTP_200_OK:
            result = json.loads(response.json())
            return Response(data=result, status=status.HTTP_200_OK)

        return Response(data={"message": response.content}, status=response.status_code)


class MockBackUrlViewSet(generics.GenericAPIView):

    def post(self, request, *args, **kwargs):
        return Response(data=request.data, status=status.HTTP_200_OK)
