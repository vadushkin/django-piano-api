from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Author, Category, Sheet, Tag
from .permissions import IsOwnerOrReadOnly
from .serializers import (
    AuthorSerializer,
    CategorySerializer,
    SheetSerializer,
    TagSerializer,
)
from .services import _get_routes, get_current_user


@api_view(["GET"])
def get_routes(_):
    routes = _get_routes()
    return Response(routes)


class SheetViewSet(viewsets.ModelViewSet):
    queryset = Sheet.objects.all()
    serializer_class = SheetSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def get_queryset(self):
        self.request.user = get_current_user(self.request)
        queryset = Sheet.objects.filter(user=self.request.user)

        return queryset

    def create(self, request, *args, **kwargs):
        request.user = get_current_user(request)
        return super().create(request, *args, **kwargs)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def create(self, request, *args, **kwargs):
        request.user = get_current_user(request)
        return super().create(request, *args, **kwargs)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def create(self, request, *args, **kwargs):
        request.user = get_current_user(request)
        return super().create(request, *args, **kwargs)


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def create(self, request, *args, **kwargs):
        request.user = get_current_user(request)
        return super().create(request, *args, **kwargs)

# @api_view(["GET", "POST"])
# def get_sheets(request):
#     match request.method:
#         case "GET":
#             return get_list_of_sheets(request)
#         case "POST":
#             return create_sheet(request)
#
#
# @api_view(["GET", "PUT", "DELETE"])
# def get_sheet(request, pk):
#     match request.method:
#         case "GET":
#             return get_sheet_details(request, pk)
#         case "PUT":
#             return update_sheet(request, pk)
#         case "DELETE":
#             return delete_sheet(request, pk)
