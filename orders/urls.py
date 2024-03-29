from django.conf.urls import url
from django.contrib.auth.forms import UserCreationForm
from django.urls import path, include
from django.views.generic import CreateView

from . import views

urlpatterns = [
    url(r"^$", views.product_list, name="product_list"),
    # url("leaderboard", views.leaderboard, name="leaderboard"),
    url(
        r"^(?P<category_slug>[-\w]+)/$",
        views.product_list,
        name="product_list_by_category",
    ),
    url(
        r"^(?P<id>\d+)/(?P<slug>[-\w]+)/$", views.product_detail, name="product_detail"
    ),
    url("^accounts/", include("django.contrib.auth.urls")),
    url("accounts/signup", views.signup_view, name="signup"),
]
