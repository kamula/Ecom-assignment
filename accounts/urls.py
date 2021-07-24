from django.urls import path
from . import views
urlpatterns = [

    path('signup',views.signup_view,name='register'),
    path('login',views.login_view,name='login'),
    path('urls',views.get_urls,name='urls'),
]

