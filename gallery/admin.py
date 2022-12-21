from django.contrib import admin
from .models import Artwork

class ArtworkAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Artwork, ArtworkAdmin)

# Register your models here.
