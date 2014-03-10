from django.contrib import admin
from gs.models import House, People, Review_Code, Review


# Register your models here.



from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User



# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class PeopleInline(admin.StackedInline):
    model = People
    can_delete = False
    verbose_name_plural = 'people'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (PeopleInline, )

class HouseAdmin(admin.ModelAdmin):
	list_display = ('unit', 'street', 'city', 'state', 'country', 'zip')

class Review_CodeAdmin(admin.ModelAdmin):
	list_display = ('factor_name', 'factor_type', 'factor_value')

class ReviewAdmin(admin.ModelAdmin):
	list_display = ('uid', 'hid', 'code', 'value')


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(House, HouseAdmin)
admin.site.register(Review_Code, Review_CodeAdmin)
admin.site.register(Review, ReviewAdmin)