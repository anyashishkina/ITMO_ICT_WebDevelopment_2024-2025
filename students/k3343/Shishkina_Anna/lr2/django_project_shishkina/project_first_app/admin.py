from django.contrib import admin
from .models import UserProfile, Homework,Submission

admin.site.register(UserProfile)
admin.site.register(Submission)
admin.site.register(Homework)


