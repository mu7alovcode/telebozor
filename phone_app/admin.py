from django.contrib import admin
from .models import Phone, Category,Contact


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'price', 'publish_time', 'status')
    list_filter = ('status', 'publish_time', 'created_time')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish_time'
    search_fields = ('title', 'bodt', 'price')
    ordering = ('status', 'publish_time')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')



admin.register(Contact)