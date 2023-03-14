from django.urls import path
from . import views
urlpatterns = [
    #### views urls
    path('',views.MalleList.as_view(),name="malle"),
    path('api/malles',views.MalleView.as_view(),name=""),
    path('api/malle/<int:id>',views.MalleViewPk.as_view(),name=''),
    path('api/femalles',views.FemalleView.as_view(),name=""),
    path('api/femalle/<int:id>',views.FemalleViewPk.as_view(),name=''),
    path('api/femalle/cage_vide',views.CageVide.as_view(),name=''),
    path('api/femalles/production',views.FemalleProductionView.as_view(),name=""),
    path('api/malle/img/<int:id>',views.MalleImageViewPk.as_view(),name=''),


]