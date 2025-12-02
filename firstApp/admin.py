from django.contrib import admin
from . import models

# Register your models here.

class GamesAdmin(admin.ModelAdmin):
    list_display = ('name', 'release_date',)
    search_fields = ('name',)
    list_filter = ('release_date',)
    filter_horizontal = ('genre',)
   
class GenresAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    # filter_horizontal = ('games',)

admin.site.register(models.Games, GamesAdmin)
admin.site.register(models.Genres, GenresAdmin)
admin.site.register(models.Detail)

