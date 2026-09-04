from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from..app.models import UserProfile

admin.site.register(UserProfile)