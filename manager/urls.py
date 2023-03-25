from django.urls import path
from . import views
urlpatterns = [
    #### views urls
    path('',views.MalleList.as_view(),name="malle"),
    path('api/malles',views.MalleView.as_view(),name=""),
    path('api/malle/<int:id>',views.MalleViewPk.as_view(),name=''),
    path('api/femalles',views.FemalleView.as_view(),name=""),
    path('api/femalle/<int:id>',views.FemalleViewPk.as_view(),name=''),
    path('api/femalle/cage_vide',views.CageVideFemalle.as_view(),name=''),
    path('api/malle/cage_vide',views.CageVideMalle.as_view(),name=''),
    path('api/femalles/production',views.FemalleProductionView.as_view(),name=""),
    path('api/malles/production',views.MalleProductionView.as_view(),name=""),

    path('api/femalle/vent/<int:id>',views.FemalleVentPk.as_view(),name=''),
    path('api/malle/vent/<int:id>',views.MalleVentPk.as_view(),name=''),
    path('api/femalle/mort/<int:id>',views.FemalleMortPk.as_view(),name=''),
    path('api/malle/mort/<int:id>',views.MalleMortPk.as_view(),name=''),






   path('groupes',views.ProductionView.as_view(),name='production'), 
   path('groupes/<int:id>',views.ProductionViewPk.as_view(),name="production_update"), 
   path('groupes/mort_masse',views.MortMasseLapinsProductionsView.as_view()),
   path('groupes/vaccin',views.VaccinProductionsView.as_view()), 
 
   path('groupes/vente_masse',views.VenteMasseLapinsProductionsView.as_view()), 
   path('groupes/groupe_sevrage/<int:id>',views.SevrageProductionsView.as_view()), 

   path('groupes/groupe_poid/',views.PoidLapinProductionsView.as_view()), 

   
   path('femalles_acouplements',views.FemallesAcouplementsView.as_view()),
   path('malles_acouplements',views.MallesAcouplementsView.as_view()),
   
   
   
   path('acouplements',views.AccouplementView.as_view(),name='accouplement'), 
   path('accouplements/<int:id>',views.AccouplementViewPk.as_view(),name="accouplement_pk"), 
   path('accouplements/test/<int:id>',views.AccouplementChangeTestView.as_view()), 
   path('accouplements/fause-couche/<int:id>',views.AccouplementFauseCoucheView.as_view()), 


   
   
   path('lapins_productions',views.LapinProductionView.as_view(),name='LapinProduction'), 
   path('lapins_productions/<int:id>',views.LapinProductionViewPk.as_view(),name="LapinProduction_pk"), 
]









