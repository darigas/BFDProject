from django.conf.urls import url
from .views import CreateUserAPIView
from . import views
from .views import TokenAuthentication

app_name = 'users'

urlpatterns = [
    url(r'create/$', CreateUserAPIView.as_view()),
    url(r'token_obtain/$', views.authenticate_user),
    # url(r'login/$', TokenAuthentication.as_view)
]
