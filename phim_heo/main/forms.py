from django import forms

class CreateListForm(forms.Form):
	name = forms.CharField(label="Name ", max_length=200)
	password = forms.CharField(label="Name ", max_length=200)