from django import forms
from meals.models import Order

class OrderForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.options = kwargs.pop('options')
        order = kwargs.pop('order', False)
        super(OrderForm, self).__init__(*args, **kwargs)
        values = []
        for option in self.options:
            values.append((option.id, option.description))

        if order:
            self.data = kwargs.pop('order')
            self.fields['option'] = forms.ChoiceField(widget=forms.Select, choices=values, initial=self.order.option)
            self.fields['customization'] = forms.CharField(max_length=170, required=False, initial=self.order.customization)
        else:
            print "self.kwargs.items():"
            # self.fields['option'] = forms.ChoiceField(widget=forms.Select, choices=values)
            # self.fields['customization'] = forms.CharField(max_length=170, required=False)
