from django.conf.urls import  url, include
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'p_int_ramajud2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.home, name='home' ),
    url(r'^authorization_request/', views.authorization_request, name='authorization_request'),
    url(r'^access_token_request/', views.access_token_request, name='access_token_request,'),    
]
