from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('all_books/', views.all_books, name='all_books'),
    path('ganre/<str:slug>', views.category_detail, name='category_detail'),
    path('pdf/<str:slug>', views.book_detail, name='book_detail'),
    path('search/', views.search_book, name='search_book'),

    path('register', views.register_page, name='register'),
    path('login', views.login_page, name='login'),
    path('logout', views.logout_user, name='logout'),
]
