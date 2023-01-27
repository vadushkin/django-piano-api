from django.urls import path

from .views import get_sheets, get_routes, get_sheet

urlpatterns = [
    path('', get_routes, name="sheets_routes"),
    path('sheet/<int:pk>/', get_sheet, name="sheet"),
    path('sheets/', get_sheets, name="sheets"),
]
