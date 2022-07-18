from django.contrib import admin
from .models import Book,  Packages
from .models import MemberUsers
from .models import Event
from django.contrib.auth import get_user_model

User = get_user_model()

# Register your models here.

# admin.site.register(Book)
# admin.site.register(MemberUsers)
#admin.site.register(Event)


@admin.register(Packages)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('name','city', 'address', 'phone')
    ordering = ('name',)
    search_fields = ('name', 'address')

@admin.register(Book)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone')
    ordering = ('name',)
    search_fields = ('name', 'address')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = (('name','venue'),'vacationDate','description','manager')
    list_display = ('name', 'vacationDate')
    list_filter = ('vacationDate', 'venue')
    ordering = ('-vacationDate',)

    
    
class MemberAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "first_name":
            kwargs["queryset"] = User.objects.filter(
                username=request.user.username
            )
        return super(MemberAdmin, self).formfield_for_foreignkey(
            db_field, request, **kwargs
        )

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            return self.readonly_fields + ("first_name",)
        return self.readonly_fields

    def add_view(self, request, form_url="", extra_context=None):
        data = request.GET.copy()
        data["first_name"] = request.user
        request.GET = data
        return super(MemberAdmin, self).add_view(
            request, form_url="", extra_context=extra_context
        )
        
    list_display = ('email', 'address', 'phone')
    ordering = ('email',)
    search_fields = ('email', 'address')


admin.site.register(MemberUsers, MemberAdmin)


