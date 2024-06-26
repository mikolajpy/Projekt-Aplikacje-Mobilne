from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path("stores/",views.ZabkaLista.as_view(),name="Zabka-view-create"),
    path("stores/<int:id>/",views.ZabkaOneShop.as_view(),name="Zabka-one-shop"),
    path('coms/', views.CommentsList.as_view() ,name="All-comments"),
    path('store/<int:store_id>/coms/', views.CommentsByStore.as_view(), name='Comments-by-store'),
    path('store/<int:store_id>/coms/<int:parent_id>/', views.CommentsByParent.as_view(), name='Comments-by-parent'),
    path('users/', views.UserList.as_view()),
    path('users/<int:user_id>/', views.UserDetail.as_view()),
    path('achievments/', views.AchievementList.as_view()),
    path('assigned/', views.AssignedList.as_view()),
    path('assigned/achievment/<int:achievment_id>/', views.AssignedListByAchievment.as_view()),
    path('assigned/user/<int:user_id>/', views.AssignedListByUser.as_view()),
    path('visited/user/<int:visitor>/', views.VisitedByUser.as_view()),
    path('visit/', views.VisitedPost.as_view()),
]