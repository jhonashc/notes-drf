from rest_framework import status, viewsets
from rest_framework.views import Response
from apps.base.pagination import CustomPagination
from apps.user.api.serializers.user_serializer import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    pagination_class = CustomPagination
    
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(is_active=True)
        return self.get_serializer().Meta.model.objects.filter(id=pk, is_active=True).first()
    
    def list(self, request):
        try:
            queryset = self.filter_queryset(self.get_queryset())
            page = self.paginate_queryset(queryset)
            
            if page is not None:
                user_serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(data=user_serializer.data)
            
            user_serializer = self.get_serializer(queryset, many=True)
            return self.get_paginated_response(data=user_serializer.data)
        except Exception as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request):
        try:
            user_serializer = self.serializer_class(data=request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def retrieve(self, request, pk=None):
        try:
            if self.get_queryset(pk):
                user_serializer = self.serializer_class(self.get_queryset(pk))
                return Response(data=user_serializer.data, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_404_NOT_FOUND)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)    

    def update(self, request, pk=None):
        try:
            if self.get_queryset(pk):
                user_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
                if user_serializer.is_valid():
                    user_serializer.save()
                    return Response(data=user_serializer.data, status=status.HTTP_200_OK)
                return Response(status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_404_NOT_FOUND)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def partial_update(self, request, pk=None):
        try:
            if self.get_queryset(pk):
                user_serializer = self.serializer_class(self.get_queryset(pk), data=request.data, partial=True)
                if user_serializer.is_valid():
                    user_serializer.save()
                    return Response(data=user_serializer.data, status=status.HTTP_200_OK)
                return Response(status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_404_NOT_FOUND)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def destroy(self, request, pk=None):
        try:
            user_serializer = self.get_queryset().filter(id=pk).first()
            if user_serializer:
                user_serializer.is_active = False
                user_serializer.save()
                return Response(status=status.HTTP_200_OK)
            return Response(status=status.HTTP_404_NOT_FOUND)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)