from django.urls import path, include
from bikes import views

urlpatterns = [    
    path('', view= views.index, name='index'),
    path('list/', view= views.all_bikes, name='all_bikes'),
    path('brands/', view= views.brands, name='brands'),
    path('count_by_brand/', view= views.counter, name='count_by_brand'),
    
]