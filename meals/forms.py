from django import forms


class OrderForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.options = kwargs.pop('options')
        super(OrderForm, self).__init__(*args, **kwargs)
        values = []
        for option in self.options:
            values.append((option.id, option.description))
        self.fields['employee_identifier'] = forms.CharField(max_length=10, min_length=1)
        self.fields['option'] = forms.ChoiceField(widget=forms.Select, choices=values)
        self.fields['customization'] = forms.CharField(max_length=170, required=False)
