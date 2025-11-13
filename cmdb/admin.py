from django.contrib import admin
from cmdb.models import host

# Register your models here.
class hostAdmin(admin.ModelAdmin):
    list_display = ("hostname","ip","disk","cpu","mem","desc")
admin.site.register(host,hostAdmin)