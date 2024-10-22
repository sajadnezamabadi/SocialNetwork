from django.contrib import admin

from .models import Friendship

# ###############################

@admin.register(Friendship)
class FriendshipAdmin(admin.ModelAdmin):
    list_display = ['request_from','request_to','is_accepted','created_time',]\
        
    # def has_add_permission(self, request):
    #     return False

    def has_delete_permission(self, request, obj=None):
        return False