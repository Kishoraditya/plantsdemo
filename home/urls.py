from django.urls import path
from .views import landing_page

urlpatterns = [
    # ... other URL patterns
    path('landing_page/', landing_page, name='landing_page'),
]
