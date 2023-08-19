from django import forms
from .models import Application, District, Branch, AccountType, Material, Gender


class Application_l(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    dob = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    age = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    gender = forms.ModelChoiceField(queryset=Gender.objects.all(), empty_label='Select District',
                                    widget=forms.Select(attrs={'class': 'form-control'}))
    district = forms.ModelChoiceField(queryset=District.objects.all(), empty_label='Select District',
                                      widget=forms.Select(attrs={'class': 'form-control'}))
    branch = forms.ModelChoiceField(queryset=Branch.objects.all(), empty_label='Select Branch',
                                    widget=forms.Select(attrs={'class': 'form-control'}))
    account_type = forms.ModelChoiceField(queryset=AccountType.objects.all(), empty_label='Select Account Type',
                                          widget=forms.Select(attrs={'class': 'form-control'}))
    materials_provide = forms.ModelMultipleChoiceField(queryset=Material.objects.all(),
                                                       widget=forms.CheckboxSelectMultiple(
                                                           attrs={'class': 'form-check-input'}),)

    # materials_provide = forms.MultipleChoiceField(choices=Material, widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        super(Application_l, self).__init__(*args, **kwargs)
        self.fields['branch'].queryset = Branch.objects.none()

        def clean(self):
            cleaned_data = super(Application_l, self).clean()
            selected_district = cleaned_data.get('district')
            if selected_district:
                self.fields['branch'].queryset = Branch.objects.filter(district=selected_district)
            return cleaned_data

