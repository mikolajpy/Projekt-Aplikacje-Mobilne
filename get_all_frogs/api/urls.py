from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("storesList/",views.ZabkaLista.as_view(),name="Zabka-view-create"),
    path("storeID=<int:id>/",views.ZabkaOneShop.as_view(),name="Zabka-one-shop"),
    path('coms/', views.CommentsList.as_view() ,name="Test"),
    path('storeID=<int:store_id>/coms', views.CommentsByStore.as_view(), name='comments-by-store'),
    path('storeID=<int:store_id>/comID=<int:parent_id>/', views.CommentsByParent.as_view(), name='comments-by-parent'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]