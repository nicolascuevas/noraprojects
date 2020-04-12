from django import forms
from meals.models import Order, Option, Menu, Employee


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [ 'option', 'customization' ]

        
    def __init__(self, **kwargs):
        super(OrderForm, self).__init__(**kwargs)
        menu =  kwargs.get("initial").get("menu")
        self.fields['option'].queryset = Option.objects.filter(menu=menu)

        


