from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication,SessionAuthentication 
from rest_framework.response import Response
from get_all_frogs.models import Zabka, StoreComment , User
from .serializers import ZabkaSerializer, CommSerializer , UserSerializer 


class ZabkaLista(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    queryset = Zabka.objects.all()
    serializer_class = ZabkaSerializer

class ZabkaOneShop(generics.RetrieveAPIView):
    queryset = Zabka.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    serializer_class = ZabkaSerializer
    lookup_field = 'id'


class CommentsByStore(generics.ListCreateAPIView):
    serializer_class = CommSerializer
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def get_queryset(self):
        store_id = self.kwargs['store_id']
        return StoreComment.objects.filter(store=store_id , parent__isnull=True)

class CommentsList(generics.ListCreateAPIView):
    serializer_class = CommSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication,SessionAuthentication]

    def perform_create(self, serializer):
        if serializer.validated_data.get('parent') is not None:
            return Response({'error': 'Cannot add a main comment with a parent.'}, status=status.HTTP_400_BAD_REQUEST)

        if serializer.validated_data.get('rating') is None:
            return Response({'error': 'Main comment must include a rating.'}, status=status.HTTP_400_BAD_REQUEST)

        existing_comment = StoreComment.objects.filter(user=self.request.user, parent__isnull=True)
        if existing_comment.exists():
            return Response({'error': 'User can only create one main comment per store.'}, status=status.HTTP_400_BAD_REQUEST)

        store_id = serializer.validated_data.get('store')
        store = get_object_or_404(Zabka, id=store_id)
        serializer.save(user=self.request.user, store=store)

    def get_queryset(self):
        return StoreComment.objects.filter(parent__isnull=True)

class CommentsByParent(generics.ListCreateAPIView):
    serializer_class = CommSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication,SessionAuthentication]

    def perform_create(self, serializer):
        parent_id = self.kwargs.get('parent_id')
        parent_comment = get_object_or_404(StoreComment, id=parent_id, parent__isnull=True)

        if serializer.validated_data.get('rating') is not None:
            return Response({'error': 'Subcomments cannot include a rating.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save(user=self.request.user, parent=parent_comment)

    def get_queryset(self):
        parent_id = self.kwargs['parent_id']
        return StoreComment.objects.filter(parent=parent_id)

class UserList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    #queryset = User.objects.all()
    serializer_class = UserSerializer
    def get_queryset(self):
        # Filter out superusers
        return User.objects.filter(is_superuser=False)


class UserDetail(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    #queryset = User.objects.all()
    serializer_class = UserSerializer
    def get_queryset(self):
        # Filter out superusers
        return User.objects.filter(is_superuser=False)
