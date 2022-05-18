
from django.urls import path

from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view()),
]

from . import apis

urlpatterns = [
    path('api/', apis.api.as_view(), name = "api")
]