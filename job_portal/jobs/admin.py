# jobs/admin.py
from django.contrib import admin
from .models import User, Job, Resume

admin.site.register(User)
admin.site.register(Job)
admin.site.register(Resume)
