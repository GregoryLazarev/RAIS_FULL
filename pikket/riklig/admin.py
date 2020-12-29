from django.contrib import admin
from .models import *

admin.site.register(author)
admin.site.register(post)
admin.site.register(comment)