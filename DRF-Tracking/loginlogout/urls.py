from .views import RegisterAPI, Login, Logout
from django.contrib import admin
from django.urls import path
from loginlogout.views import ObtainJWTView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', view=ObtainJWTView.as_view(), name='login'),
]
urlpatterns = [
    path('register/', RegisterAPI.as_view(), name="register"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
]
