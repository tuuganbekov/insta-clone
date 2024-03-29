from django.urls import path

from users.views import register_page, login_page, logout_user, index, cabinet, profile, search_users, follow_operation

app_name = 'users'

urlpatterns = [
    path('', index, name='index'),
    path('register/', register_page, name='register'),
    path('login/', login_page, name='login'),
    path('logout/', logout_user, name='logout'),
    path('cabinet/', cabinet, name='cabinet'),
    path('profile/<int:id>/', profile, name='profile'),
    path('<int:id>/', follow_operation, name='follow_operation'),
    path('results/', search_users, name='search-users'),
]
