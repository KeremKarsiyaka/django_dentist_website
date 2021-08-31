from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
	return render (request, 'home.html', {})


def contact(request):
	if request.method == "POST":
		message_name = request.POST['name']
		message_email = request.POST['email']
		message = request.POST['comments']

		send_mail(
			message_name,
			message,
			message_email,
			['keremkarsiyakaa@gmail.com'],
			)
		
		return render(request, 'contact.html', {'message_name': name})

	else:
		return render (request, 'contact.html', {})

	
def pricing(request):
	return render (request, 'pricing.html', {})


