from django.contrib import admin
from.models import User,Events

# Register your models here.


class UserImp(admin.ModelAdmin):
    list_display = ('username','is_Service_provider' )
class EventImp(admin.ModelAdmin):
    list_display = ('title', 'description', )


admin.site.register(User, UserImp)
admin.site.register(Events, EventImp)