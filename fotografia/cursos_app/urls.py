from django.contrib import admin
from django.urls import path , include

from .router import router

from .views import      CursosListView   \
                    ,   CursosDetailView \
                    ,   CursosCreateView \
                    ,   CursosUpdateView \
                    ,   CursosDeleteView

app_name = "cursos"

urlpatterns = [
    path("", CursosListView.as_view(), name="all"),
    path("create/", CursosCreateView.as_view(), name="create"),
    path("<int:pk>/detail/", CursosDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", CursosUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", CursosDeleteView.as_view(), name="delete")
]

urlpatterns += router.urls