from rest_framework import generics
from .serializers import ImiModelSerializer
from imi_status.models import ImiStatus
from django.db.models import Q
from rest_framework import permissions
from .pagination import StandardResultPagination
##Create you view  down below

class ImiListApiView(generics.ListAPIView):
    queryset = ImiStatus.objects.all()
    pagination_class = StandardResultPagination
    serializer_class = ImiModelSerializer
    def  get_queryset(self,*args,**kwargs):
        qs = ImiStatus.objects.all().order_by('-timestamp')
        query = self.request.GET.get('q',None)
        if query is not None:
            qs = qs.filter(
                Q(content__icontains = query) |
                Q(user__username__icontains= query) 
            )
        return qs

class ImiCreateApiView(generics.CreateAPIView):
    serializer_class = ImiModelSerializer
    permissions.classes = [permissions.IsAuthenticated]
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)
    