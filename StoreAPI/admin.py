from django.contrib import admin
from . import models


class RatingAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


class ParishIdPeek(admin.ModelAdmin):
    readonly_fields = ('id',)


class VillagePeek(admin.ModelAdmin):
    readonly_fields = ('parish',)


class DivisionPeek(admin.ModelAdmin):
    readonly_fields = ('district',)


# Register your models here.
admin.site.register(models.Product)
admin.site.register(models.Review)
admin.site.register(models.Banner)
admin.site.register(models.Tag)
admin.site.register(models.District)
admin.site.register(models.Division)
admin.site.register(models.Parish)
admin.site.register(models.Village)
admin.site.register(models.Street)
admin.site.register(models.UserToken)
admin.site.register(models.Order)
