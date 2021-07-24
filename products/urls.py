from django.urls import path
from . import views


urlpatterns = [
    path('',views.product_view,name='product'),
    path('categories',views.create_category,name='categories'),
    
]

