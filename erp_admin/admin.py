from django.contrib import admin
from erp_admin.models import *
# Register your models here.
class mainannouncementsAdmin(admin.ModelAdmin):

    list_display = ('title', 'desc', 'click_count','date_publish',)
    list_display_links = ('title', 'desc', )
    list_editable = ('click_count',)

    fieldsets = (
        (None, {
            'fields': ('title', 'desc', 'content', )
        }),
        ('高级设置', {
            'classes': ('collapse',),
            'fields': ('click_count', 'is_recommend',)
        }),
    )
    
admin.site.register(Mainannouncements,mainannouncementsAdmin)