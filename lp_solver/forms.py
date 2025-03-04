from django import forms

from django import forms

class LPForm(forms.Form):
    # Define your form fields here
    field1 = forms.CharField(max_length=100)
    field2 = forms.IntegerField()
field3 = forms.EmailField()

class LinearProgrammingForm(forms.Form):
    objective_function = forms.CharField(label='Objective Function (e.g., 3x + 5y)', max_length=100)
    constraints = forms.CharField(
        label='Constraints (one per line, e.g., x + 2y <= 8)',
        widget=forms.Textarea(attrs={'rows': 5})
    )
