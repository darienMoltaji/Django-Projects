from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("todo/", include("todo_list_app.urls")),
    path("admin/", admin.site.urls),
]
