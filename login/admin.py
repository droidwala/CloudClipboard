from django.contrib import admin
from login.models import Page,Category,UserProfile

admin.site.register(Category)
admin.site.register(Page)
admin.site.register(UserProfile)
