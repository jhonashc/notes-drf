from rest_framework import viewsets

class BaseViewSet(viewsets.ModelViewSet):
    def get_queryset(self, pk=None, is_user=False):
        if is_user:
            if pk is None:
                return self.get_serializer().Meta.model.objects.filter(is_active=True).order_by('id')
            return self.get_serializer().Meta.model.objects.filter(id=pk, is_active=True).first()
        
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(status=True).order_by('id')
        
        return self.get_serializer().Meta.model.objects.filter(id=pk, status=True).first()
            