from django.contrib import admin
from .models import Costomer
# Register your models here.

class CostomerAdmin(admin.ModelAdmin):
    list_display = ('robot_page','company_name','robot_key','contact','contact_title','tel','mobile','fax','address','post_code','website','create_time','update_time')
    search_fields = ('company_name','contact','tel','address')
    list_filter = ('robot_key',)

admin.site.register(Costomer,CostomerAdmin)