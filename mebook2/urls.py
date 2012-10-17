from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from mebook2.views import home_m, contact
from django.contrib import admin
from registration.forms import RegistrationFormUniqueEmail
from book.models import Seria, Author, Book
from book.views import search, knigi, book_get
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


urlpatterns = patterns('',
	(r'^$', home_m),
    (r'^search/$', search),
    (r'^books/s(\d{1,4})/$', knigi),
    (r'^books/s(\d{1,4})/(\d{1,4})$', book_get),
    (r'^books/a(\d{1,4})/$', knigi),
    (r'^contact/$', contact),
    url(r'^register/$', 'registration.views.register', {'form': RegistrationFormUniqueEmail}, name='registration_register'),
    (r'^accounts/', include('registration.urls')),
    # Examples:
    # url(r'^$', 'mybook.views.home', name='home'),
    # url(r'^mybook/', include('mybook.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
if settings.DEBUG:
	urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.STATIC_ROOT}),
         (r'^media_file/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
        )

