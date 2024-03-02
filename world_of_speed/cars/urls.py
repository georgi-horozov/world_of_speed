from django.urls import path


from world_of_speed.cars.views import CreateCarView, catalogue_view, DetailCarView, EditCarView, DeleteCarView

urlpatterns = [

    path("create/", CreateCarView.as_view(), name="create_car"),
    path("catalogue/", catalogue_view, name="catalogue_view"),
    path("<int:pk>/details/", DetailCarView.as_view(), name='details_car'),
    path("<int:pk>/edit/", EditCarView.as_view(), name='edit_car'),
    path("<int:pk>/delete/", DeleteCarView.as_view(), name='delete_car'),

]