from django.urls import path
from .views import(
    show
)

urlpatterns = [
    path('', show.as_view()),
]
