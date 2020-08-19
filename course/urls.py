from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('subjectsbyclass/',views.subjects_by_class, name='class-subjects'),
    path('chaptersbysubject/',views.chapters_by_subject, name='subject-chapters'),
    path('topicsbychapter/',views.topics_by_chapter, name='chapter-topics'),
    path('homepage.html/',views.get_home, name='home-page'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', views.index, name='login'),
    path('',views.index, name='index'),
]