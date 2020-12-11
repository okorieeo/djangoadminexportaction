from admin_export_action.admin import export_selected_objects
from django.contrib import admin 
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('export_action/', include("admin_export_action.urls", namespace="admin_export_action")),
]
