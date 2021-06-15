from django import forms


class HomeForm(forms.Form):
	Name = forms.CharField()
	Birth date= forms.CharField()
	Age = forms.CharField()


