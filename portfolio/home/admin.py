from django.contrib import admin

# Register your models here.
from .models import ContactMessage

admin.site.register(ContactMessage)
