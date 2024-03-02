from django.urls import path

from world_of_speed.profile_app.views import DetailProfileView, UpdateProfileView, DeleteProfileView, CreateProfileView

urlpatterns = (
    # path('create/', create_profile, name='create_profile'),
    path('create/', CreateProfileView.as_view(), name='create_profile'),
    path("details/", DetailProfileView.as_view(), name="details_profile"),
    path("edit/", UpdateProfileView.as_view(), name='edit_profile'),
    path("delete/", DeleteProfileView.as_view(), name='delete_profile'),
)