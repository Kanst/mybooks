# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from book.models import Seria, Author, Book
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin 
from django.template import RequestContext

def home_m(request):
    len_serias = range(len(Seria.objects.all()))
    sp_serias = Seria.objects.all()
    sp_autors = Author.objects.all()
    return render_to_response('index.html', {'len_serias': len_serias, 'title':'Библиотека Kanst9',
                                                    'sp_serias': sp_serias, 'sp_autors': sp_autors,}, context_instance=RequestContext(request))

def contact(request):
	len_serias = range(len(Seria.objects.all()))
	sp_serias = Seria.objects.all()
	sp_autors = Author.objects.all()
	return render_to_response('contact.html', {'len_serias': len_serias, 'title':'Библиотека Kanst9',
                                                    'sp_serias': sp_serias, 'sp_autors': sp_autors,})


