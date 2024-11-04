from django.contrib.auth.models import User
from django.shortcuts import render


def homepage(request):
    return render(request ,'HomePage.html')
def StudentHomePage(request):
    return render(request, 'studentapp/StudentHomePage.html')
from facultyapp.models import Marks
from adminapp.models import StudentList
def view_mark(request):
    user=request.user
    try:

        student_user=User.objects.get(username=user.username)
        student=StudentList.objects.get(Register_Number =student_user)
        marks=Marks.objects.filter(student=student)
        return render(request, 'studentapp/view_marks.html',{'marks':marks})
    except (StudentList.DoesNotExist, User.DoesNotExist):
        return render(request,'studentapp/no_studentlist.html',{
            'error':'No Student record found for this user.'
        })