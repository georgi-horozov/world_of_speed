from django import forms
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from world_of_speed.cars.models import Car
from world_of_speed.profile_app.models import Profile


def get_profile():
    return Profile.objects.first()
class CarFormMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['type'].widget = forms.TextInput(attrs={'placeholder': 'Type'})
        form.fields['model'].widget = forms.TextInput(attrs={'placeholder': 'Model'})
        form.fields['year'].widget = forms.Textarea(attrs={'placeholder': 'Year'})
        form.fields['image_url'].widget = forms.URLInput(attrs={'placeholder': 'Image URL'})
        form.fields['price'].widget = forms.NumberInput(attrs={'placeholder': 'Price'})
        return form

class CreateCarView(CarFormMixin, views.CreateView):
    queryset = Car.objects.all()
    template_name = 'cars/car-create.html'
    fields = ['type', 'model', 'year', 'image_url', 'price']
    success_url = reverse_lazy('catalogue_view')

    def form_valid(self, form):
        form.instance.owner_id = get_profile().pk
        return super().form_valid(form)


def catalogue_view(request):
    # Check if the user has a profile
    has_profile = get_profile()

    # Retrieve all cars from the database
    cars = Car.objects.all() if has_profile else []

    context = {
        'has_profile': has_profile,
        'cars': cars,
    }

    return render(request, 'web/catalogue.html', context=context)


class DetailCarView(views.DetailView):
    queryset = Car.objects.all()
    template_name = 'cars/car-details.html'
    fields = ("image_url", "type", "model", "year")


class EditCarView(CarFormMixin, views.UpdateView):
    queryset = Car.objects.all()
    template_name = 'cars/car-edit.html'
    fields = ['type', 'model', 'year', 'image_url', 'price']
    success_url = reverse_lazy("catalogue_view")


class DeleteCarView(views.DeleteView):
    queryset = Car.objects.all()
    template_name = 'cars/car-delete.html'
    success_url = reverse_lazy("catalogue_view")







