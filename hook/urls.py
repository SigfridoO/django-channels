from django.urls import path

from .views import hookView

urlpatterns = [
    path('', hookView.as_view(), name='hook'),
    
]