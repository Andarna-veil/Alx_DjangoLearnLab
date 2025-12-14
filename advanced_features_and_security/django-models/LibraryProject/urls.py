from django.contrib import admin
from django.urls import path, include  # include is needed to reference app urls

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin
    path('', include('relationship_app.urls')),  # include your app's URLs
]
