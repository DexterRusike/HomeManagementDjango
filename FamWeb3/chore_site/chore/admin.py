from django.contrib import admin
from chore.models import UserProfileInfo, TimesheetEntry, loan_personal_info

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(TimesheetEntry)
admin.site.register(loan_personal_info)


