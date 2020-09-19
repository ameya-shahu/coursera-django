from django.contrib import admin

# Register your models here.
from ads.models import Ad


class AdAdmin(admin.ModelAdmin):
    exclude = ('picture', 'content_type')


admin.site.register(Ad, AdAdmin)
