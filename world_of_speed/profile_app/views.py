# from django import forms
# from django.shortcuts import render
# from django.urls import reverse_lazy
from django.db import models
# from django.forms import PasswordInput, forms
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic as views
from django import forms


from world_of_speed.cars.models import Car


from world_of_speed.profile_app.models import Profile



def get_profile():
    return Profile.objects.first()


# def create_profile(request):
#     form = CreateProfileForm(request.POST or None)
#
#     if form.is_valid():
#         form.save()
#         return redirect("catalogue_view")
#
#     context = {
#         "form": form,
#         # "no_nav": True,
#     }
#
#     return render(request, template_name="profile_app/profile-create.html", context=context)

class CreateProfileView(views.CreateView):
    queryset = Profile.objects.all()
    template_name = 'profile_app/profile-create.html'
    fields = ['username', 'email', 'age', 'password']
    success_url = reverse_lazy('catalogue_view')

    widgets = {
        'username': forms.TextInput(attrs={'placeholder': 'Username'}),
        'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
        'age': forms.NumberInput(attrs={'placeholder': 'Age'}),
        'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
    }

class DetailProfileView(views.DetailView):
    queryset = Profile.objects.all()
    template_name = "profile_app/profile-details.html"

    def get_object(self, queryset=None):
        return get_profile()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Retrieve the profile object
        profile = get_profile()

        # Calculate the total price of all cars associated with the profile
        # total_car_price = Car.objects.filter(owner=profile).aggregate(total_price=models.Sum('price'))['total_price']
        cars = Car.objects.filter(owner=profile)

        total_car_price = sum(car.price for car in cars)

        # Pass the total car price to the template context
        context['total_car_price'] = total_car_price

        return context


class UpdateProfileView(views.UpdateView):
    queryset = Profile.objects.all()
    template_name = "profile_app/profile-edit.html"
    fields = ('username', 'email', 'age', 'password', 'first_name', 'last_name', 'profile_picture')
    success_url = reverse_lazy('details_profile')

    def get_object(self, queryset=None):
        return get_profile()


class DeleteProfileView(views.DeleteView):
    template_name = 'profile_app/profile-delete.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_profile()




