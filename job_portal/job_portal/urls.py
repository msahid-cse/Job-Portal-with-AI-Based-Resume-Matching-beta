# """
# URL configuration for job_portal project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/5.1/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# # job_portal/urls.py
# from django.contrib import admin
# from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # Add your app URLs here
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

# job_portal/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render

# Define a view to render the home.html page
def home(request):
    return render(request, 'jobs/home.html')  # Your home page template

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # Home page
    path('', home, name='home'),  # This will render home.html

    # Include the job portal URLs for registration, login, and logout
    path('jobs/', include('jobs.urls')),  # Include the URLs from your jobs app

    # Include Django's authentication URLs (login, logout, etc.)
    path('accounts/', include('django.contrib.auth.urls')),  # Django's built-in auth URLs
]

# Serve static and media files in development (only if settings.DEBUG is True)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
