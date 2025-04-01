from django.contrib import admin
from django.urls import path
from theater_app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path("", views.home, name="home"),
    path("showtimes/", views.showtimes, name='showtimes'),
    path("coming_soon/", views.coming_soon, name='coming_soon'),
    path('contact/', views.contact, name='contact'),
    path('login_register/', views.login_register, name='login_register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login_register'), name='logout'),
    path('ticket_purchase/<int:showtime_id>/', views.ticket_purchase, name='ticket_purchase'),
    path('movie_details/<int:movie_id>/', views.movie_details, name='movie_details'),
    path('register', views.register, name='register'),

]

