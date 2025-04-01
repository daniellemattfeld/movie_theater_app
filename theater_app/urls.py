from django.urls import path
from theater_app import views


urlpatterns = [
    path('', views.home, name='home'),
    path('', views.showtimes, name='showtimes'),
    path('', views.coming_soon, name='coming_soon'),
    path('', views.contact, name='contact'),
    path('', views.login_register, name='login_register'),
    path('', views.logout, name='logout'),
    path('', views.ticket_purchase, name='ticket_purchase'),
    path('', views.movie_details, name='movie_details'),
    path('', views.register, name='register'),

]


