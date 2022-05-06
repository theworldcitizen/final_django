import logging

import rest_framework.generics as generics
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from auth_.models import MainUser, Profile
from auth_.serializers import UserSerializer, ProfileSerializer

logger = logging.getLogger(__name__)


class CreateUserViewSet(viewsets.ModelViewSet):
    queryset = MainUser.objects.all()
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.action == 'create':
            return UserSerializer

    @action(methods=['POST'], detail=False, permission_classes=(AllowAny,))
    def post_user(self, request):
        user = request.data
        queryset = MainUser.objects.create_user(email=user['email'], password=user['password'],
                                                first_name=user['first_name'], last_name=user['last_name'],
                                                role=user['role'])
        queryset.save()
        logger.debug(f'User created ID: {user}')
        logger.info(f'User created ID: {user}')
        logger.warning(f'User created ID: {user}')
        logger.error(f'User created ID: {user}')
        logger.critical(f'User created ID: {user}')
        return Response(user, status=status.HTTP_201_CREATED)


class ProfileApiViewSet(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (AllowAny,)
    queryset = Profile.objects.all()
    parser_classes = [FormParser, JSONParser, MultiPartParser]
