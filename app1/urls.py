from django.urls import path
from app1.views import home, add_student,success, dashboard,student_record_view,update_student, delete_student, course

urlpatterns = [
    path('', home, name ='home'),
    path('add/',add_student, name='add'),
    path('success/', success , name='success'),
    path('dashboard/', dashboard , name='dashboard'),
    path('student', student_record_view, name='student_record_view'),
    path('update/<int:id>/', update_student, name='update_student'),
    path('delete/<int:id>/', delete_student,  name = 'delete_student'),
    path('course/', course , name='course')
]
