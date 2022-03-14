from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework.viewsets import ModelViewSet
from .models import Post
from django.contrib.auth import get_user_model

# Create your views here.

class PostViewSet(ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer