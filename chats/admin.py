from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(PrivateMessages)
admin.site.register(Conversation)
admin.site.register(Participants)
admin.site.register(ConversMessages)