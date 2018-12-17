from django.shortcuts import render , render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from testing.models import *
import testing.my_method

def index(request):
    student = Student.objects.filter(isDeleted=False)
    stu = []
    for i in student:
        stu.append(i.name)
    context = {'list':stu}
    return render(request, 'index.html', context)

def index_handle(request):
    uname = request.POST['uname']
    request.session['myname'] = uname
  #  request.session['myid'] = id
    request.session.set_expiry(50000)  #save session 1000 sec.
    return HttpResponseRedirect('/testing/')

def session_out(request):
    try:
        del request.session['myname']
    except:
        pass
    return HttpResponseRedirect('/')

# def tes(request):
#     return HttpResponse(testing.my_method.sort_ranking())