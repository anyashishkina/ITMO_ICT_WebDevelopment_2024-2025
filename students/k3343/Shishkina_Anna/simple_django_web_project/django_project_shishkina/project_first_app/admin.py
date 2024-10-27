from django.contrib import admin
from .models import Owner, Ownership, Car, License

admin.site.register(Owner)
admin.site.register(Car)
admin.site.register(Ownership)
admin.site.register(License)
