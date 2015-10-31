from django.contrib import admin

# Register your models here.
from users.models import *

admin.site.register(User) # this line makes the table 'User' available to localhost/admin