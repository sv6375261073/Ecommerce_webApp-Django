from django.contrib import admin

from .models  import Teacher,Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('Name', 'DOB')


admin.site.register(Teacher),
admin.site.register(Student, StudentAdmin)



