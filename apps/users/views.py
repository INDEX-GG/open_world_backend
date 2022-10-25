from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer
from rest_framework.response import Response
from rest_framework import status


class UserRegistrationAPIView(APIView):
    serializer_class = UserRegistrationSerializer

    def post(self, requests):
        serializer = self.serializer_class(data=requests.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)
