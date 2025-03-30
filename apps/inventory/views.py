from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def admin_dashboard(request):
    return render(request, "inventory/admin_dashboard.html")

@login_required
def manager_dashboard(request):
    return render(request, "inventory/manager_dashboard.html")

@login_required
def staff_dashboard(request):
    return render(request, "inventory/staff_dashboard.html")
