from django.http import HttpResponse
from django.shortcuts import render

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
	context = {
		"title": "Contact",
		"content": "Welcome to my contacts!"
	}
	if request.method == 'POST':
		#print(request.POST)
		print(request.POST.get('full_name'))
		print(request.POST.get('email'))
		print(request.POST.get('content'))
	return render(request, 'contact/view.html', context)