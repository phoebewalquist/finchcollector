from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finches_index, name='index'),
    path('finches/<int:finche_id>/', views.finches_detail, name='detail'),
    path('finches/create/', views.FincheCreate.as_view(), name='finches_create'),
    path('finches/<int:pk>/update/', views.FincheUpdate.as_view(), name='finches_update'),
    path('finches/<int:pk>/delete/', views.FincheDelete.as_view(), name='finches_delete'),

]
