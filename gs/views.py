from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

# Create your views here.

from django.http import HttpResponse

@login_required
def index(request):
    return render_to_response('gs/index.html',context_instance=RequestContext(request))

@login_required
def comparison(request):
    return render_to_response('gs/comparison.html',context_instance=RequestContext(request))

@login_required
def dashboard(request):
    return render_to_response('gs/comparison.html',context_instance=RequestContext(request))

@login_required
def allhomes(request):
    return render_to_response('gs/comparison.html',context_instance=RequestContext(request))

@login_required
def myhomes(request):
    return render_to_response('gs/comparison.html',context_instance=RequestContext(request))




def reviews(request, review_id):
	return "You are looking for review number %s."  % review_id