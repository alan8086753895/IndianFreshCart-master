from django import forms
from .models import Profile,Product,Order


class Profileform(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude=['user']

class Productform(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ['user']

class Orderform(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"
        exclude=['user']