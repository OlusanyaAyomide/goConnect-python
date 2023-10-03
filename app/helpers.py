from django.shortcuts import get_object_or_404
from .models import CustomUser,MessageModel

def get_last_two_message(username):
    custom_user = CustomUser.objects.get(username=username)

    message_count = custom_user.message.count()

    # Check if the total count is at least 2
    if message_count >= 2:

        last_two_messages = custom_user.message.order_by('createdAt')[:2]
        return last_two_messages
    else:
        return None

