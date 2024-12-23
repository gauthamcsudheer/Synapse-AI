from django.urls import path
from . import views

app_name = 'ocr'

urlpatterns = [
    path('', views.ocr_view, name='upload'),  # OCR upload page
]
