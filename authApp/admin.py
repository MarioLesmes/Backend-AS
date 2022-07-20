from django.contrib import admin
from .models.user   import User
from .models.aS     import AS

admin.site.register(User)
admin.site.register(AS)