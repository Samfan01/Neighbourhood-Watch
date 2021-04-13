from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[
    path('',views.home,name = 'home'),
    path('profile',views.profile,name = 'profile'),
    path('update_profile',views.update_profile,name = 'update_profile'),
    path('hood/<int:neighbourhood_id>/',views.hood,name='hood'),
    path('new_post/',views.new_post,name = 'new_post'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)