from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required

# Create your views here.

from django.http import HttpResponse

@login_required
def index(request):
    return render_to_response('gs/index.html')

def reviews(request, review_id):
	return "You are looking for review number %s."  % review_id