from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:item_id>", views.viewitem, name="viewitem"),
    path("viewcart", views.viewcart, name="viewcart"),
    path("viewcat/<str:catname>", views.viewcat, name="viewcat"),
    path("wish", views.wish, name="wish"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("creatlisting", views.newlisting, name="creatlisting"),
    path("wishlist", views.wishlist, name="wishlist"),
    path("newlisting", views.newitem, name="newlisting"),
    path("endauction", views.end_auction, name="endauction"),
    path("catpage", views.catpage, name="catpage"),
    path("newbid", views.newbid, name="newbid"),
    path("newcomment", views.newcomment, name="newcomment"),
    path("register", views.register, name="register")
]
