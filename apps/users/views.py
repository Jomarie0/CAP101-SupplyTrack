from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib.auth import login, logout
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .models import User
from .serializer import UserRegistrationSerializer, UserSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            tokens = response.data

            access_token = tokens.get("access")
            refresh_token = tokens.get("refresh")

            res = Response({"success": True})

            res.set_cookie(
                key="access_token",
                value=access_token,
                httponly=True,
                secure=True,
                samesite=None,
                path="/",
            )

            res.set_cookie(
                key="refresh_token",
                value=refresh_token,
                httponly=True,
                secure=True,
                samesite=None,
                path="/",
            )

            return res
        except:
            return Response({"success": False}, status=400)

class CustomRefreshTokenView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.COOKIES.get('refresh_token')

            if not refresh_token:
                return Response({'refreshed': False}, status=400)

            request.data['refresh'] = refresh_token
            response = super().post(request, *args, **kwargs)

            tokens = response.data
            access_token = tokens.get('access')

            if not access_token:
                return Response({'refreshed': False}, status=400)

            res = Response({'refreshed': True})
            res.set_cookie(
                key='access_token',
                value=access_token,
                httponly=True,
                secure=True,
                samesite=None,
                path='/'
            )
            return res
        except:
            return Response({'refreshed': False}, status=400)
        
        
def register_view(request):
    success = False  # Flag to indicate registration success
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            success = True  # Set success flag to True
            return render(request, "users/register.html", {"form": form, "success": success})

    else:
        form = CustomUserCreationForm()

    return render(request, "users/register.html", {"form": form, "success": success})

def redirect_based_on_role(user):
    if user.role == "admin":
        return redirect("inventory:admin_dashboard")
    elif user.role == "manager":
        return redirect("inventory:manager_dashboard")
    elif user.role == "staff":
        return redirect("inventory:staff_dashboard")
    else:
        return redirect("inventory:staff_dashboard") 

def login_view(request):
    if request.user.is_authenticated:
        return redirect_based_on_role(request.user)  
    
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect_based_on_role(user)
        else:
            messages.error(request, "Invalid username or password.")
    
    else:
        form = AuthenticationForm()
    
    return render(request, "users/login.html", {"form": form})



@api_view(['POST'])
def logout(request):
    try:
        res = Response()
        res.data = {'success': True}
        res.delete_cookie('access_token', path='/', samesite='None')
        res.delete_cookie('refresh_token', path='/', samesite='None')
        return res   
    except:
        return Response({'success': False}, status=400)
    
def logout_view(request):
    logout(request)  
    request.session.flush()  
    return redirect("users:login")

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def is_authenticated(request):
    return Response({'authenticated': True})

@login_required
def dashboard_view(request):
    return render(request, "users/dashboard.html", {"user": request.user})