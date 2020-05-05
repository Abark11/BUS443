from django.shortcuts import render
from django.http import HttpResponse
from studentinfo.models import Coursedetails
from studentinfo.models import Studentdetails
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    return render(request, 'studentinfo/home.html')

@login_required
def studentdetails(request):
    return render(request, 'studentinfo/studentdetails.html')

@login_required
def studentenrollment(request):
    return render(request, 'studentinfo/studentenrollment.html')

@login_required
def coursedetails(request):
    return render(request, 'studentinfo/coursedetails.html')

@login_required
def coursedetailsinfo(request):
    coursedata = Coursedetails.objects.all()
    paginator = Paginator(coursedata, 10)
    page = request.GET.get('page')
    coursedetailsminiset = paginator.get_page(page)
    return render(request, 'studentinfo/coursedetailsinfo.html', {'cdata':coursedetailsminiset})

@login_required   
def studentdetailsinfo(request):
    studentdata = Studentdetails.objects.all()
    paginator = Paginator(studentdata, 10)
    page = request.GET.get('page')
    studentdetailsminiset = paginator.get_page(page)
    return render(request, 'studentinfo/studentdetailsinfo.html', {'sdata':studentdetailsminiset})

def savedata(request):
    if('studentid' and 'courseid' in request.GET):
        studentid = int(request.GET.get('studentid'))
        courseid = int(request.GET.get('courseid'))
        adddata = Enrollmentdetails(studentid=studentid, courseid=courseid)
        adddata.save()
        return HttpResponse('Success')
    
