from django.contrib import admin
from .models import Flavor
from django.urls import reverse
from django.utils.html import format_html

class FlavorAdmin(admin.ModelAdmin):
    list_display = ("title","body","created",)
    readonly_fields = ("show_url",)

    def show_url(self, instance):
        url =reverse("detail",
            kwargs={"pk": instance.pk})
        response = format_html("""<a href="{0}">{1}</a>""",url,url)
        return response
    
    show_url.short_description = "flavor url"
    show_url.allow_tag = True
    
admin.site.register(Flavor,FlavorAdmin)