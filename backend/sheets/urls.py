from django.urls import path, include
from rest_framework import routers

from .views import SheetViewSet, AuthorViewSet, TagViewSet, CategoryViewSet, get_routes  # , get_sheet, get_sheets

router = routers.SimpleRouter()

router.register(r"sheets", SheetViewSet)
router.register(r"categories", CategoryViewSet)
router.register(r"tags", TagViewSet)
router.register(r"authors", AuthorViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("", include(router.urls)),
    path("", include(router.urls)),
    # path("", get_routes, name="sheets_routes"),
    # path("sheet/<int:pk>/", get_sheet, name="sheet"),
    # path("sheets/", get_sheets, name="sheets"),
]
