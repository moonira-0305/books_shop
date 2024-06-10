from .views import books_list, books_detail, HomePageView
from django.urls import path,include

urlpatterns=[
    path("",HomePageView,name="home_page"),
    path("books/",books_list, name="all_books_list"),
    path("books/<int:id>/",books_detail,name="books_detail_page"),

]