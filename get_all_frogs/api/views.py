from django.shortcuts import render
from rest_framework import generics, status
from get_all_frogs.models import Zabka,StoreComment
from .serializers import ZabkaSerializer, CommSerializer

class ZabkaLista(generics.ListCreateAPIView):
    queryset = Zabka.objects.all()
    serializer_class = ZabkaSerializer

class ZabkaListaDelete(generics.RetrieveAPIView):
    queryset = Zabka.objects.all()
    serializer_class = ZabkaSerializer
    lookup_field = 'name'

class CommentsList(generics.ListAPIView):
    serializer_class = CommSerializer
    
    def get_queryset(self):
        return StoreComment.objects.filter(parent__isnull=True)

class CommentsByStore(generics.ListCreateAPIView):
    serializer_class = CommSerializer
    
    def get_queryset(self):
        store_id = self.kwargs['store_id']
        return StoreComment.objects.filter(store=store_id)

class CommentsByParent(generics.ListCreateAPIView):
    serializer_class = CommSerializer
    
    def get_queryset(self):
        parent_id = self.kwargs['parent_id']
        return StoreComment.objects.filter(parent=parent_id)