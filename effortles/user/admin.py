from django.contrib import admin
from .models import User, Department, Designation, Profile, Address, UserSalaryRecord, AppliedLeave, Leave
from .forms import CustomeUserCreationForm
from django.contrib.auth.admin import UserAdmin


class CustomeUserAdmin(UserAdmin):
    model: User
    add_form: CustomeUserCreationForm

    fieldsets = (
        *UserAdmin.fieldsets,
    )


admin.site.register(User)
admin.site.register(Department)
admin.site.register(Designation)
admin.site.register(Profile)
admin.site.register(Address)
admin.site.register(UserSalaryRecord)
admin.site.register(AppliedLeave)
admin.site.register(Leave)
