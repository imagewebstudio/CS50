from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("register_cashier/<str:store>/", views.register_cashier, name="register_cashier"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("profile", views.profile, name="profile"),
    path("pos/<str:store>/", views.pos_register, name="pos_register"),
    path("stores/<int:create>", views.stores, name="stores"),
    path("stores", views.stores, name="stores"),
    path("make_item/<str:store>/", views.create_item, name="make_item"),
    path("lookup/", views.lookup, name="lookup"),
    path("checkout/", views.checkout, name="checkout"),
    path("reciept_lookup/", views.rec_lookup, name="reciept_lookup"),
    path("lookup_name/", views.lookup_name, name="lookup_name"),
    path("store_settings/<str:store>/", views.store_settings, name="store_settings"),
    path("store_settings/<str:store>/<str:setting>", views.store_settings, name="settings"),
    path("poss", views.login_pos, name="poss"),
    path("update_set/", views.settings_functions, name="update_set"),

    # API Routes

]
