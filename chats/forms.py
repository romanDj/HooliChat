from django import forms
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm

class UserForm(forms.Form):
	login = forms.CharField(
		label='Login:', 
		max_length=50, 
		widget= forms.TextInput(attrs={
			'class' : "form-control",
			'required': "true",
			'autocomplete':"off"}))
	password = forms.CharField(
		label='Password:', 
		max_length=50, 
		widget=forms.PasswordInput(attrs={
			'class' : "form-control",
			'required': "true",
			'autocomplete':"off"}))


class RegisterFormView(FormView):
	form_class = UserCreationForm
	success_url = "../"
	template_name = "chats/registration.html"

	def form_valid(self, form):
		form.save()
		return super(RegisterFormView, self).form_valid(form)