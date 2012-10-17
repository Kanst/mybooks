# -*- coding: utf-8 -*-
from django.db import models

class Seria(models.Model):
    name = models.CharField('Название серии', max_length=30)

    def __unicode__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField('Фамилия', max_length=30)
    last_name = models.CharField('Имя', max_length=40)
    email = models.EmailField('e-mail', blank = True)
    headshot = models.ImageField(upload_to='foto_autor/', blank = True)

    def __unicode__(self):
        return '%s %s' % (self.last_name, self.first_name)

class Book(models.Model):
    title = models.CharField('название', max_length=100)
    authors = models.ManyToManyField(Author, blank = True)
    serias = models.ForeignKey(Seria, blank = True)
    add_date = models.DateField('дата добавления', null=True, auto_now_add=True)
    res_date = models.DateField('дата последнего изменения', null=True, auto_now=True)
    pub_date = models.DateField('дата публикации', null=True, blank = True)
    oblojka = models.ImageField(upload_to='imag_book/', blank = True, default='imag_book/none.jpg')
    annotation = models.TextField('аннотация', blank = True, default='Описание отсутствует(')
    podseria = models.CharField('серия автора', blank = True, max_length=20)
    url_l = models.URLField(blank = True)
    book_file = models.FileField(upload_to='books/', blank = True, null=True)
    def __unicode__(self):
        return self.title