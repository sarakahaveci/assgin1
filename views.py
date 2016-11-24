from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponseRedirect,render_to_response,HttpResponse,Http404


# Create your views here.

from models import *
def data(request):
    listAppend=[]
    for key,value in myCourses.items():
        listAppend.append(value[0])

    return render_to_response('printData.html',{'listAppend':listAppend})
def getData(request,key):


    try:

            return HttpResponse(myCourses[int(key)][1])
    except IndexError:
        raise Http404("We don't have any.")
