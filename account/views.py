from django.shortcuts import render, redirect
from .forms import UserCreationForm
from .models import MyUser
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib import messages

# home page view
class HomePageView(TemplateView):
    template_name = 'home.html'

# User signup view
class UserSignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "register.html"

# User login view
class Userloginviews(LoginView):
    template_name = 'login.html'
    
    def get_success_url(self):
        return reverse_lazy('home')

# user profile
@login_required
def view_profile(request):
    # Retrieve the current user's profile
    profile = request.user
    return render(request, 'profile.html', {'profile': profile})


class userlogoutview(View):
    def get(self, request):
        logout(request)
        messages.success(self.request, 'Logout Successfully. Welcome Back!')
        return redirect('home')