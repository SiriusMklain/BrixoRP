"""
URL configuration for RP_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app3.views import CustomLoginView
from app4.views import VisitToTTView, EditVisitToTTView, EditSlide, NewSlide, ViewRept, DeleteSlide, AddedRept

urlpatterns = [
    path('admin/', admin.site.urls),
    path('visit/', include('app.urls')),
    path('report/', include('app2.urls')),

    path('login/', CustomLoginView.as_view(), name='login'),
    path('list/', VisitToTTView.as_view(), name='visit-to-tt-list'),
    path('rept/<int:pk>/', EditVisitToTTView.as_view(), name='visit-to-tt-edit'),
    path('added-rept/', AddedRept.as_view(), name='added-rept'),

    path('view/<int:pk>/', ViewRept.as_view(), name='view-rept'),
    path('delete-slide/<int:slide_id>/<int:pk>/', DeleteSlide.as_view(), name='delete-slide'),

    path('edit-visit-to-tt/edit-slide/<int:slide_id>/', EditSlide.as_view(), name='visit-to-tt-edit-slide'),
    path('edit-visit-to-tt/new-slide/', NewSlide.as_view(), name='new-slider-data'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
