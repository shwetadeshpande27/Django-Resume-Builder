from django.urls import path

from .views import (
    home,
    create_resume,
    edit_resume,
    resume_preview,
)


urlpatterns = [

    path(
        "",
        home,
        name="home"
    ),

    path(
        "create/",
        create_resume,
        name="create_resume"
    ),

    path(
        "edit/<int:resume_id>/",
        edit_resume,
        name="edit_resume"
    ),

    path(
        "preview/<int:resume_id>/",
        resume_preview,
        name="resume_preview"
    ),
]