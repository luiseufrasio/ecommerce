from django.contrib.auth import authenticate, login, get_user_model

from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ContactForm, LoginForm, RegisterForm

def home_page(request):
	context = {
		"title": "Hello World",
		"content": "Welcome my friend!"
	}
	if request.user.is_authenticated:
		context["premium_content"] = "YAHOOOOO!"
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
			return redirect("/")
		else:
			print("Error")
	
	return render(request, "auth/login.html", context)

User = get_user_model()
def register_page(request):
	form = RegisterForm(request.POST or None)
	context = {
		"form": form
	}
	if form.is_valid():
		print(form.cleaned_data)
		username=form.cleaned_data["username"]
		email=form.cleaned_data["email"]
		password=form.cleaned_data["password"]
		new_user = User.objects.create_user(username, email, password)
		print(new_user)
	return render(request, "auth/register.html", context)