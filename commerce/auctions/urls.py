from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('listings/<int:item_id>', views.show_item, name="item"),
    path('listings/<int:item_id>/bid', views.save_bid, name="bids"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
]
