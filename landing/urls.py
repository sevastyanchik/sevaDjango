from django.urls import path
from .views import MyLessonsView,MyLessonsDetailView
from django.views.generic.base import TemplateView
from .views import BlogView,BlogUpdate,BlogDelete


urlpatterns = [
    path('', MyLessonsView.as_view(
        template_name="landing/index.html"
    ), name='home'),
    path('<int:pk>/', MyLessonsDetailView.as_view(), name='mylesson-detail'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('about/', TemplateView.as_view(template_name='landing/about.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='landing/contact.html'), name='contact'),
    path('<int:pk>/update/', BlogUpdate.as_view(), name='blog_update'),
    path('<int:pk>/delete/', BlogDelete.as_view(), name='blog_delete'),

]