from django.contrib import admin
from .models import Student
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class StudentResources(resources.ModelResource):
    class Meta:
        model = Student 

@admin.register(Student)
class BookAdmin(ImportExportModelAdmin):
    list_display = [ 'name', 'age', 'city', 'course', 'price', 'date']
    resource_class = StudentResources