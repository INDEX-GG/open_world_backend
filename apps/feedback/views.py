from rest_framework import generics, status
from rest_framework.response import Response

from apps.feedback.serializers import FeedbackSerializer, QuestionsSerializer, FeedbackMessageSerializer
from apps.feedback.models import Questions
from apps.feedback.utils import Util, SendFeedbackMessage
from apps.base.permissions import IsAdminOrReadOnly


class FeedbackAPIView(generics.GenericAPIView):
    serializer_class = FeedbackSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        created = Util.send_feedback_mail(data)
        if created:
            return Response({'result': True}, status=status.HTTP_200_OK)
        else:
            return Response({'result': False, 'email': ['Ошибка отправления']}, status=status.HTTP_404_NOT_FOUND)


class QuestionsAPIView(generics.ListAPIView):
    queryset = Questions.objects.all().order_by('-pk')
    serializer_class = QuestionsSerializer
    permission_classes = (IsAdminOrReadOnly,)


class QuestionsItemAPIView(generics.RetrieveAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer
    permission_classes = (IsAdminOrReadOnly,)


def post(self, request):
    serializer = self.serializer_class(data=request.data)
    serializer.is_valid(raise_exception=True)
    data = serializer.validated_data
    try:
        created = SendFeedbackMessage.send_feedback_mail(data)
        if created:
            return Response(True, status=status.HTTP_200_OK)
        else:
            return Response(False, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response(False, status=status.HTTP_404_NOT_FOUND)
