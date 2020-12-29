from django.urls import path
from . import views

urlpatterns = [
    # path('', views.placeholder, name = "home"),
    path('', views.home_page, name = "home"),
    path('login/', views.login_page, name = "login"),
    path('logout/', views.logout_user, name = "logout"),
    path('register/', views.register_page, name = "register"),
    path('newpost/', views.create_post, name = "create_post"),
    path('update_post/<str:pk>', views.update_post, name = "update_post"),
    path('delete_post/<str:pk>', views.delete_post, name = "delete_post"),
    path('get_post/<str:pk>', views.get_post_data, name = "get_post_data"),
    path('my_posts/', views.my_posts, name = "my_posts")
]
