# from django.shortcuts import get_object_or_404
# from rest_framework.response import Response
#
# from .models import Sheet
# from .serializers import SheetSerializer
#
#
# def get_list_of_sheets(_):
#     sheets = Sheet.objects.all().order_by("-updated_at")
#     serializer = SheetSerializer(
#         instance=sheets,
#         many=True,
#     )
#     return Response(serializer.data)
#
#
# def get_sheet_details(_, pk):
#     serializer = SheetSerializer(
#         instance=get_object_or_404(Sheet, pk=pk),
#         many=False,
#     )
#     return Response(serializer.data)
#
#
# def create_sheet(request):
#     serializer = SheetSerializer(data=request.data)
#
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response(serializer.errors)
#
#
# def update_sheet(request, pk):
#     serializer = SheetSerializer(
#         instance=get_object_or_404(Sheet, pk=pk),
#         data=request.data,
#     )
#
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response(serializer.errors)
#
#
# def delete_sheet(_, pk):
#     get_object_or_404(Sheet, pk=pk).delete()
#     return Response("Sheet was deleted!")
from django.conf import settings
import jwt

from users.models import User


def _get_routes():
    routes = [
        {
            "Endpoint": "/sheets/",
            "method": "GET",
            "body": None,
            "description": "Returns an array of sheets",
        },
        {
            "Endpoint": "/sheets/",
            "method": "POST",
            "body": {
                "name": "Require",
                "user": "Require",
                "file_pdf": "Require",
                "author": "Not Require",
                "description": "Not Require",
                "category": "Not Require",
                "tags": "Not Require",
            },
            "description": "Creates new sheet with data sent in post request",
        },
        {
            "Endpoint": "/sheet/:id",
            "method": "GET",
            "body": None,
            "description": "Returns a single sheet object",
        },
        {
            "Endpoint": "/sheet/:id",
            "method": "PUT",
            "body": {
                "name": "",
                "user": "",
                "file_pdf": "",
                "author": "",
                "description": "",
                "category": "",
                "tags": "",
            },
            "description": "Creates an existing sheet with data sent in post request",
        },
        {
            "Endpoint": "/sheets/:id",
            "method": "DELETE",
            "body": None,
            "description": "Deletes and exiting sheet",
        },
        {
            "Endpoint": "/categories/",
            "method": "GET",
            "body": None,
            "description": "Returns an array of categories",
        },
        {
            "Endpoint": "/categories/",
            "method": "POST",
            "body": {
                "name": "Require",
                "slug": "Not Require",
                "user": "Require",
            },
            "description": "Creates new category with data sent in post request",
        },
        {
            "Endpoint": "/categories/:id",
            "method": "GET",
            "body": None,
            "description": "Returns a single category object",
        },
        {
            "Endpoint": "/categories/:id",
            "method": "PUT",
            "body": {
                "name": "",
                "slug": "",
                "user": "",
            },
            "description": "Creates an existing category with data sent in post request",
        },
        {
            "Endpoint": "/categories/:id",
            "method": "DELETE",
            "body": None,
            "description": "Deletes and exiting category",
        },
        {
            "Endpoint": "/tags/",
            "method": "GET",
            "body": None,
            "description": "Returns an array of tags",
        },
        {
            "Endpoint": "/tags/",
            "method": "POST",
            "body": {
                "name": "Require",
                "slug": "Not Require",
                "user": "Require",
            },
            "description": "Creates new tag with data sent in post request",
        },
        {
            "Endpoint": "/tags/:id",
            "method": "GET",
            "body": None,
            "description": "Returns a single tag object",
        },
        {
            "Endpoint": "/tags/:id",
            "method": "PUT",
            "body": {
                "name": "",
                "slug": "",
                "user": "",
            },
            "description": "Creates an existing tag with data sent in post request",
        },
        {
            "Endpoint": "/tags/:id",
            "method": "DELETE",
            "body": None,
            "description": "Deletes and exiting tag",
        },
        {
            "Endpoint": "/authors/",
            "method": "GET",
            "body": None,
            "description": "Returns an array of authors",
        },
        {
            "Endpoint": "/authors/",
            "method": "POST",
            "body": {
                "name": "Require",
                "slug": "Not Require",
                "user": "Require",
            },
            "description": "Creates new author with data sent in post request",
        },
        {
            "Endpoint": "/authors/:id",
            "method": "GET",
            "body": None,
            "description": "Returns a single author object",
        },
        {
            "Endpoint": "/authors/:id",
            "method": "PUT",
            "body": {
                "name": "",
                "slug": "",
                "user": "",
            },
            "description": "Creates an existing author with data sent in post request",
        },
        {
            "Endpoint": "/authors/:id",
            "method": "DELETE",
            "body": None,
            "description": "Deletes and exiting author",
        },
    ]
    return routes


def get_current_user(request):
    """Get the current user on request"""
    token = request.COOKIES.get("jwt")

    if not token:
        return False

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return False

    user = User.objects.filter(id=payload["id"]).first()
    return user
