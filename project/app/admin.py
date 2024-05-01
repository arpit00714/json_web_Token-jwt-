from django.contrib import admin
from .models import MovieModel

# Register your models here.
@admin.register(MovieModel)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id','title','description']