from django.contrib import admin
from .models import SpecialRooms, HotelMembers
from django.contrib.auth.models import User

# Register your models here.

#admin.site.register(SpecialRooms)
#admin.site.register(HotelMembers)

@admin.register(SpecialRooms)
class SpecialAdmin(admin.ModelAdmin):
    list_display = ('hotelName','address', 'phone')
    ordering = ('hotelName',)
    search_fields = ('hotelName','address')

    
class PostAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "last_name":
            kwargs["queryset"] = User.objects.filter(
                username=request.user.username
            )
        return super(PostAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs
        )

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            return self.readonly_fields + ("last_name",)
        return self.readonly_fields

    def add_view(self, request, form_url="", extra_context=None):
        data = request.GET.copy()
        data["last_name"] = request.user
        request.GET = data
        return super(PostAdmin, self).add_view(
            request, form_url="", extra_context=extra_context
        )
        
    list_display = ('last_name', 'inDate', 'outDate', 'roomNo')
    ordering = ('last_name',)
    search_fields = ('last_name', 'address')


admin.site.register(HotelMembers, PostAdmin)

