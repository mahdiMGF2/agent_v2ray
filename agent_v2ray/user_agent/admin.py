from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(PanelInfo)
class PanelInfoAdmin(admin.ModelAdmin):
    list_display = ('id',   'name_panel','url_panel',)
    list_display_links = ('id', 'name_panel',)

@admin.register(UserAgent)
class UserAgentAdmin(admin.ModelAdmin):
    list_display = ('user','limit_volume','limit_user')


@admin.register(Account_agent)
class Account_agentAdmin(admin.ModelAdmin):
    list_display = ('user','panel','username','created_at')

@admin.register(Log_UserAgent)
class LogUserAgentAdmin(admin.ModelAdmin):
    list_display = ('user','change_at','log_info',)
