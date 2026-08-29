
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core.views import home, submit_contact, submit_career



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('submit-contact/', submit_contact, name='submit_contact'),
    path('submit-career/', submit_career, name='submit_career'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)