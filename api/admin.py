from django.contrib import admin

from api.models import AuthorModel


class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(AuthorModel, AuthorAdmin)
