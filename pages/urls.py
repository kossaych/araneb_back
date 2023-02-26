from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index',),
    path('cour/<int:id>',views.cour,name='cour',),
    path('about',views.about,name="about")
]