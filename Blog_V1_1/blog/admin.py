from django.contrib import admin

# Register your models here.
from blog.models import Test, Contact, Tag

admin.site.register([Test, Contact, Tag])
