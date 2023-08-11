from django.contrib import admin
<<<<<<< HEAD
from .models import Tag

# Register your models here.


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ['label']
=======

# Register your models here.
>>>>>>> a77aecced6d01cf351118df2ea482b17fbe03da9
