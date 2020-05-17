"""crawler_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

# from django.conf.urls import url, include

# urlpatterns = [
#     url(r'^crawler/crawlArticle', include('crawler.urls')),
# ]

from django.conf import settings
from django.conf.urls import url, static
from django.views.generic import TemplateView
from crawler import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^api/crawl/', views.crawl, name='crawl'),
    url(r'^api/getCrawledData/', views.getCrawledData, name='getCrawledData'),
]

# This is required for static files while in development mode. (DEBUG=TRUE)
# No, not relevant to scrapy or crawling :)
# if settings.DEBUG:
#     urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
