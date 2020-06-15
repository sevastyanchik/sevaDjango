from django.urls import path
from .views import MyLessonsView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', MyLessonsView.as_view(
        template_name="landing/index.html"
    ), name='home'),
    path('about/', TemplateView.as_view(template_name='landing/about.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='landing/contact.html'), name='contact')


]