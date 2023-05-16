from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    lsist_display = ('user', 'date_of_birth', 'photo')

admin.site.register(Profile)