from rest_framework import status, viewsets
from rest_framework.views import Response
from apps.base.pagination import CustomPagination
from apps.note.api.serializers.note_serializer import NoteSerializer

class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    pagination_class = CustomPagination

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(status=True)
        return self.get_serializer().Meta.model.objects.filter(id=pk, status=True).first()

    def list(self, request):
        try:
            queryset = self.filter_queryset(self.get_queryset())
            page = self.paginate_queryset(queryset)
            
            if page is not None:
                note_serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(data=note_serializer.data)
            
            note_serializer = self.get_serializer(queryset, many=True)
            return self.get_paginated_response(data=note_serializer.data)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request):
        try:
            note_serializer = self.serializer_class(data=request.data)
            if note_serializer.is_valid():
                note_serializer.save()
                return Response(status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, pk=None):
        try:
            if self.get_queryset(pk):
                note_serializer = self.serializer_class(self.get_queryset(pk))
                return Response(data=note_serializer.data, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_404_NOT_FOUND)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
        try:
            if self.get_queryset(pk):
                note_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
                if note_serializer.is_valid():
                    note_serializer.save()
                    return Response(data=note_serializer.data, status=status.HTTP_200_OK)
                return Response(status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_404_NOT_FOUND)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def partial_update(self, request, pk=None):
        try:
            if self.get_queryset(pk):
                note_serializer = self.serializer_class(self.get_queryset(pk), data=request.data, partial=True)
                if note_serializer.is_valid():
                    note_serializer.save()
                    return Response(data=note_serializer.data, status=status.HTTP_200_OK)
                return Response(status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_404_NOT_FOUND)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, pk=None):
        try:
            note_serializer = self.get_queryset().filter(id=pk).first()
            if note_serializer:
                note_serializer.status = False
                note_serializer.save()
                return Response(status=status.HTTP_200_OK)
            return Response(status=status.HTTP_404_NOT_FOUND)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
