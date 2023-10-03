from django.contrib import admin
from .models import CustomUser, MessageModel

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(MessageModel)