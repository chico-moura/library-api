from django.contrib import admin

from api.models import AuthorDTOModel


class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(AuthorDTOModel, AuthorAdmin)
