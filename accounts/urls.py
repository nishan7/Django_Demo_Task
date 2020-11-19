
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

app_name = 'accounts'
urlpatterns = [
    path('login/', login_view, name="login"),
    path('signup/', signup, name="signup"),
    path("logout/", logged_out, name="logout")

]
