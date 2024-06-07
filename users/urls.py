from django.urls import path
from .views import UpdateProfilePictureView, UserCreateView, UserDetailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('signup/', UserCreateView.as_view(), name='user-create'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile-picture/', UpdateProfilePictureView.as_view(), name='update_profile_picture'),
    path('me/', UserDetailView.as_view(), name='user-detail'),
]
