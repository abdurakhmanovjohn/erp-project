from django.urls import path
from .views import dashboard_redirect, login_view, logout_view



urlpatterns = [
    path('dashboard/', dashboard_redirect, name='dashboard'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

]


