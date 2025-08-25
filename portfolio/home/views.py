from django.shortcuts import render
from .models import ContactMessage
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if not name or not email or not message:
            return HttpResponse("All fields are required!", status=400)

        # Save to database first
        contact_message = ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )

        subject = f"New contact message from {name}"
        full_message = f"Message: {message}\nFrom: {name}\nEmail: {email}"

        try:
            send_mail(
                subject,
                full_message,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
                fail_silently=False
            )
        except BadHeaderError:
            return HttpResponse("Invalid header found.", status=400)
        except Exception as e:
            return HttpResponse(f"Error sending email: {e}", status=500)

        return render(request, "main/index.html", {"success": True})

    return render(request, "main/index.html")
