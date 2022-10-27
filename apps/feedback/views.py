from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from .serializers import FeedbackSerializer
from .utils import Util


class FeedbackAPIView(generics.GenericAPIView):
    serializer_class = FeedbackSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        email = serializer.validated_data['email']
        Util.send_feedback_mail(data)
        return Response({"email": email, 'result': True}, status=status.HTTP_200_OK)
