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
