from django.urls import path
from .views import admin_dashboard, manager_dashboard, staff_dashboard

app_name = "inventory"

urlpatterns = [
    path("admin-dashboard/", admin_dashboard, name="admin_dashboard"),
    path("manager-dashboard/", manager_dashboard, name="manager_dashboard"),
    path("staff-dashboard/", staff_dashboard, name="staff_dashboard"),
]
