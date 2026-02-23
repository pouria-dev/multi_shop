from django.urls import path
from .views import Login_View

app_name = 'accounts'

urlpatterns = [
    path('login/' , Login_View.as_view() , name='login'),

    
]