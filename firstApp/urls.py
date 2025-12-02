from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('games/', views.games, name='games'),
    path('games/<int:game_id>/', views.game_detail, name='game_detail'),
    path('info/',views.info,name="info"),
    path('model_info/',views.model_form_info,name="model_info"),
    path('info_success/<str:name>/<int:age>/<str:email>/<str:address>/',views.info_success,name="info_success"),
    
]