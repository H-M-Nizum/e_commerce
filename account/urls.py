from django.urls import path
from .views import HomePageView, Userloginviews, UserSignUpView, view_profile, userlogoutview 

urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),
    path('register/', UserSignUpView.as_view(), name='register'),
    path('login/', Userloginviews.as_view(), name='login'),
    path('logout/',  userlogoutview.as_view(), name='logout'),
    path('profile/', view_profile, name='view_profile'),
]