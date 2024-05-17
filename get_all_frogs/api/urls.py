from django.urls import path
from . import views

urlpatterns = [
    path("",views.ZabkaLista.as_view(),name="Zabka-view-create"),
    path("<name>/",views.ZabkaListaDelete.as_view(),name="Zabka-delete"),
]