from django.contrib import admin
from home.models import Contact, Pay, Slot
from home.views import contact
# from home.views import contact
# Register your models here.

admin.site.register(Contact)

admin.site.register(Slot)

# admin.site.register(Checkbox)

admin.site.register(Pay)