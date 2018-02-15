from django.conf.urls import url
from first_web_app import views

# NAMESPACE
app_name = 'first_web_app'

urlpatterns = [
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^register/$', views.register, name='register'),
]
