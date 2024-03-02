# from django import forms
#
# from world_of_speed.profile_app.models import Profile
#
#
# class CreateProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['username', 'email', 'age', 'password']
#
#         widgets = {
#             'username': forms.TextInput(attrs={'placeholder': 'Username'}),
#             'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
#             'age': forms.NumberInput(attrs={'placeholder': 'Age'}),
#             'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
#         }
