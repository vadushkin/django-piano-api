from django.urls import path

from .views import get_routes, get_sheet, get_sheets

urlpatterns = [
    path("", get_routes, name="sheets_routes"),
    path("sheet/<int:pk>/", get_sheet, name="sheet"),
    path("sheets/", get_sheets, name="sheets"),
]
