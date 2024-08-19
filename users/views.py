from djoser.views import UserViewSet
from .paginators import UserPaginator
from .serializers import CurrentUserSerializer, User


class UsersViewSet(UserViewSet):
    serializer_class = CurrentUserSerializer
    queryset = User.objects.all()
    pagination_class = UserPaginator
