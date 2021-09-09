from django.contrib.auth import authenticate, login

from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ContactForm, LoginForm

def home_page(request):
	context = {
		"title": "Hello World",
		"content": "Welcome my friend!"
	}
	return render(request, 'home_page.html', context)

def about_page(request):
	context = {
		"title": "About",
		"content": "Welcome to my description!"
	}
	return render(request, 'home_page.html', context)

def contact_page(request):
	contact_form = ContactForm(request.POST or None)
	context = {
		"title": "Contact",
		"content": "Welcome to my contacts!",
		"form": contact_form
	}
	if contact_form.is_valid():
		print(contact_form.cleaned_data)
	return render(request, 'contact/view.html', context)

def login_page(request):
	form = LoginForm(request.POST or None)
	context = {
		"form": form
	}
	print("User logged in:")
	print(request.user.is_authenticated)
	if form.is_valid():
		print(form.cleaned_data)
		username=form.cleaned_data["username"]
		password=form.cleaned_data["password"]
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			#context["form"] = LoginForm()
			return redirect("/login")
		else:
			print("Error")
	
	return render(request, "auth/login.html", context)

def register_page(request):
	form = LoginForm(request.POST or None)
	if form.is_valid():
		print(form.cleaned_data)
	return render(request, "auth/register.html", {})