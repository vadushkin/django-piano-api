
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .services import get_sheet_details, create_sheet, \
    get_list_of_sheets, update_sheet, delete_sheet


@api_view(['GET'])
def get_routes(_):
    routes = [
        {
            'Endpoint': '/sheets/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of sheets'
        },
        {
            'Endpoint': '/sheets/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single sheet object'
        },
        {
            'Endpoint': '/sheets/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new sheet with data sent in post request'
        },
        {
            'Endpoint': '/sheets/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing sheet with data sent in post request'
        },
        {
            'Endpoint': '/sheets/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting sheet'
        },
    ]

    return Response(routes)


@api_view(['GET', 'POST'])
def get_sheets(request):
    match request.method:
        case 'GET':
            return get_list_of_sheets(request)
        case 'POST':
            return create_sheet(request)


@api_view(['GET', 'PUT', 'DELETE'])
def get_sheet(request, pk):
    match request.method:
        case 'GET':
            return get_sheet_details(request, pk)
        case 'PUT':
            return update_sheet(request, pk)
        case 'DELETE':
            return delete_sheet(request, pk)