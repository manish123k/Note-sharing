from django.contrib import admin

from notes.models import Signup
from .models import *
# Register your models here.

admin.site.register(Signup)
admin.site.register(Notes)
