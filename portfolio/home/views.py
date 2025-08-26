from django.shortcuts import render
from django.http import HttpResponse
from .models import ContactMessage
from .service import send_email
from django.conf import settings

# Replace this with your admin email
ADMIN_EMAIL = "admin@gmail.com"


def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if not name or not email or not message:
            return HttpResponse("All fields are required!", status=400)

        # Save message into database
        ContactMessage.objects.create(name=name, email=email, message=message)

        # --- Email to Admin (you) ---
        subject_admin = f"📩 New Contact Message from {name}"
        full_message_admin = f"""
Hello Admin,

You have received a new contact message from your website.

─────────────────────────────
👤 Name: {name}
📧 Email: {email}
💬 Message:
{message}
─────────────────────────────

Please reply to this message at: {email}
"""
        # --- Auto-reply to User ---
        subject_user = "✅ Thanks for contacting us!"
        full_message_user = f"""
Hello {name},

Thank you for reaching out to us. We have received your message and will get back to you soon.

Here is a copy of your message:
─────────────────────────────
{message}
─────────────────────────────

Best regards,  
Your Support Team
"""

        try:
            # Send to admin
            send_email(
                to=ADMIN_EMAIL,
                subject=subject_admin,
                message=full_message_admin
            )

            # Send acknowledgment to user
            send_email(
                to=email,
                subject=subject_user,
                message=full_message_user
            )

        except Exception as e:
            return HttpResponse(f"Error sending email: {e}", status=500)

        return render(request, "main/index.html", {"success": True})

    return render(request, "main/index.html")
