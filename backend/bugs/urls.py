from django.contrib.auth import views as auth_views
from django.urls import path

from .views import (
    bug_create_view,
    bug_delete_view,
    bug_edit_view,
    dashboard_view,
    register_view,
    improve_description_view,
)


urlpatterns = [
    path("", dashboard_view, name="dashboard"),

    path(
        "register/",
        register_view,
        name="register",
    ),

    path(
        "accounts/login/",
        auth_views.LoginView.as_view(
            template_name="registration/login.html"
        ),
        name="login",
    ),

    path(
        "accounts/logout/",
        auth_views.LogoutView.as_view(),
        name="logout",
    ),

    path(
        "bugs/add/",
        bug_create_view,
        name="bug_create",
    ),

    path(
        "bugs/<int:pk>/edit/",
        bug_edit_view,
        name="bug_edit",
    ),

    path(
        "bugs/<int:pk>/delete/",
        bug_delete_view,
        name="bug_delete",
    ),
    path(
    "bugs/improve-description/",
    improve_description_view,
    name="improve_description",
    ),
]
