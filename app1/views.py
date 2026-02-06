from django.shortcuts import render,redirect
from .models import Student

# Create your views here.

from django.db.models import Q # Multiple filters ke liye Q use karna best hai

def student_record_view(request):
    """
    Is function ka naam 'student_record_view' rakha hai.
    Ye function search handle karega aur table mein data dikhayega.
    """
    search_query = request.GET.get('search', '') # Search text lena
    
    if search_query:
        # Q objects se logic 'OR' ban jata hai (Name OR City OR Course)
        students = Student.objects.filter(
            Q(name__icontains=search_query) | 
            Q(city__icontains=search_query) | 
            Q(course__icontains=search_query)
        ).distinct()
    else:
        students = Student.objects.all().order_by('-id') # Newest students pehle
        
    context = {
        'students': students,
        'search_query': search_query,
    }
    
    return render(request, 'app1/dashboard.html', context)

def home(request):
    return render(request,'app1/index.html')


def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        city = request.POST.get('city')
        course = request.POST.get('course')
        price = request.POST.get('price')
        date = request.POST.get("date")

        Student.objects.create(
            name = name ,
            age = age,
            city = city,
            course = course,
            price = price,
            date = date,
        )
        return redirect('success')
    return render(request,'app1/add-student.html')

def success(request):
    return render(request,'app1/success.html')  

def dashboard(request):
    # return render(request,'app1/dashboard.html')
    students = Student.objects.all()
    total = students.count()
    context = {
        'students': students,
        'total': total,
    }   
    return render(request,'app1/dashboard.html',context)

def update_student(request, id):
    obj = Student.objects.get(id=id)

    if request.method == "POST":
        obj.name = request.POST.get('name')
        obj.age = request.POST.get('age')
        obj.city = request.POST.get('city')
        obj.course = request.POST.get('course')
        obj.price = request.POST.get('price')
        obj.date = request.POST.get('date')
        obj.save()
        return redirect('success')
    return render( request, 'app1/update.html', {'student': obj})  
#'student' will go to template and show in  value (fields) then show data

def delete_student(request, id):
    obj = Student.objects.get(id =id)
    obj.delete()
    return redirect('dashboard')


def course(request):
    return render(request, 'app1/Course.html')


        