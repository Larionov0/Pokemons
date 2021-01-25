from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, authentication_classes

from auth_sys.models import UserProfile
from .serializers import UserProfileSerializer


@api_view(['GET'])
def users(request):
    user_profiles = UserProfile.objects.all()
    serializer = UserProfileSerializer(user_profiles, many=True)

    return Response({'users': serializer.data})
