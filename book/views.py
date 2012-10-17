# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import Http404
from book.models import Seria, Author, Book
from book.forms import ContactForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import list_detail
import datetime


def pagination_sokr(request,page):
    books_list = request
    paginator = Paginator(books_list, 5)
    try:
        request = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        request = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        request = paginator.page(paginator.num_pages)
    return request


def knigi(request, offset):
    #Вывод информации слева
    len_serias = range(len(Seria.objects.all()))
    sp_autors = Author.objects.all()
    sp_serias = Seria.objects.all()
    tes = request.path
    tes = tes.split('/')[2][0]
    if tes == 's':
        if int(offset) == 0:
            sp_books = pagination_sokr(Book.objects.all(), request.GET.get('page'))
            title = "Все книги"
            return list_detail.object_list(
                    request,
                    queryset = Book.objects.all(),
                    template_name = "books/books.html",
                    template_object_name = "books",
                    extra_context = {'len_serias': len_serias, 'title': title, 'sp_serias': sp_serias, 
                                    'offset': offset, 'sp_autors': sp_autors, 'sp_books': sp_books}
                )
        else:
            serias_i = 0
            pr_serias = Seria.objects.all()
            pr_serias_id = []
            for x in sp_serias:
                if x.id == int(offset):
                    serias_i = x
                    title = x.name
                pr_serias_id.append(x.id)
            if int(offset) in pr_serias_id:
                serias_i = serias_i.book_set.all()
                serias_i = pagination_sokr(serias_i, request.GET.get('page'))
                
                return list_detail.object_list(
                    request,
                    queryset = Book.objects.all(),
                    template_name = "books/books.html",
                    template_object_name = "books",
                    extra_context = {'len_serias': len_serias, 'title': title, 'sp_serias': sp_serias, 
                                    'offset': offset, 'sp_autors': sp_autors, 'sp_books': serias_i }
                    )
            else:
                raise Http404()

    elif tes == 'a':
        pr_autors = Author.objects.all()
        pr_autors_id = []
        for x in pr_autors:
            if x.id == int(offset):
                autors_i = x
                title = autors_i
            pr_autors_id.append(x.id)
        if int(offset) in pr_autors_id:
            autors_i = autors_i.book_set.all()
            serias_i = pagination_sokr(autors_i, request.GET.get('page'))
                
            return list_detail.object_list(
                request,
                queryset = Book.objects.all(),
                template_name = "books/books.html",
                template_object_name = "books",
                extra_context = {'len_serias': len_serias, 'title': title, 'sp_serias': sp_serias, 
                                'offset': offset, 'sp_autors': sp_autors, 'sp_books': serias_i }
                )
        else:
            raise Http404() 

    else:
        raise Http404()


def book_get(request, offset, allset):
    #Вывод информации слева
    len_serias = range(len(Seria.objects.all()))
    sp_autors = Author.objects.all()
    sp_serias = Seria.objects.all()
    tes = request.path
    tes = tes.split('/')[3]

    book = Book.objects.get(id=tes)
    title = book.title
    return list_detail.object_list(
                request,
                queryset = Book.objects.all(),
                template_name = "books/books_get.html",
                template_object_name = "books",
                extra_context = {'len_serias': len_serias, 'title': title, 'sp_serias': sp_serias, 
                                'offset': offset, 'sp_autors': sp_autors, 'book':book }
                )


def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('books/books.html', {'books': books, 'query': q})
    return render_to_response('books/books.html', {'error': error})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            
    else:
        form = ContactForm()
    return render_to_response('contact_form.html', {'form': form})