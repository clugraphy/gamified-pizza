from django import forms

from orders_management.models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "first_name",
            "last_name",
            "nickname",
            "email",
            "address",
            "postal_code",
            "city",
        ]
