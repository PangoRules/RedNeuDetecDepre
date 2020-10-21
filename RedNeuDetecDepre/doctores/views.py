from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def docHome(request):
	return HttpResponse('Hola doctor')