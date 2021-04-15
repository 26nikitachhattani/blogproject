"""channel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import re_path
from django.views.static import serve

vue_urls = [
  path('', lambda request: HttpResponse(render(request, 'vue_index.html'))),
  path('another-path/', lambda request: HttpResponse(render(request, 'vue_index.html'))),
]


urlpatterns = [
    path('', include('blogs.urls')),
    path('api/post/', include('blogs.api.urls')),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('profiles/api/profiles', include('profiles.api.urls')),
    path('admin/', admin.site.urls),
    path('', include(vue_urls)),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

#url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),


if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]