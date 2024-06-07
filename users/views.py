from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .models import CustomUser
from .serializers import UserSerializer

class UserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class UpdateProfilePictureView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    parser_classes = [JSONParser]
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        user = self.request.user
        profile_image_url = request.data.get('profile_image')

        if profile_image_url:
            user.profile_image = profile_image_url
            user.save()
            return Response({'profile_image': user.profile_image})
        else:
            return Response({'error': 'No profile image URL provided'}, status=400)

class UserDetailView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = self.request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)
