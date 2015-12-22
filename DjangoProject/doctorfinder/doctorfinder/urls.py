
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import *

from website import views

email_re = '[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}'

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^searchResults', views.search_results, name='search_results'),
    url(r'^signup', views.sign_up, name='sign_up'),
    url(r'^login', views.login, name='login'),
    url(r'^doctor/(?P<pk>' + email_re + ')/$', views.doctor_detail, name='doctor_detail'),
    url(r'^addReview/(?P<pk>' + email_re + ')/$', views.add_review, name='add_review'),
    url(r'^doc/(?P<pk>' + email_re + ')/$', views.add_favorite, name='add_favorite'),
    url(r'^myProfile', views.my_profile, name='my_profile'),
    url(r'^removeFavDoc/(?P<pk>' + email_re + ')/$', views.remove_favdoc, name='remove_favdoc'),
    url(r'^editPatientProfile', views.edit_patprofile, name='edit_patprofile'),
    url(r'^editDoc/(?P<pk>' + email_re + ')/$', views.edit_docprofile, name='edit_docprofile'),
]
