from rest_framework.decorators import api_view
from rest_framework.response import Response

from .services import (
    create_sheet,
    delete_sheet,
    get_list_of_sheets,
    get_sheet_details,
    update_sheet,
)

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
]


@api_view(["GET"])
def get_routes(_):
    return Response(routes)


@api_view(["GET", "POST"])
def get_sheets(request):
    match request.method:
        case "GET":
            return get_list_of_sheets(request)
        case "POST":
            return create_sheet(request)


@api_view(["GET", "PUT", "DELETE"])
def get_sheet(request, pk):
    match request.method:
        case "GET":
            return get_sheet_details(request, pk)
        case "PUT":
            return update_sheet(request, pk)
        case "DELETE":
            return delete_sheet(request, pk)
