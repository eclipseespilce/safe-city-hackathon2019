from django.urls import path
from mapApi import views

app_name = 'mapApi'

urlpatterns = [
    path('api/points/', views.add_point, name='add_point'),
    path('api/points/<str:groupId>', views.points_by_group, name='points_by_group'),
    path('api/groups/', views.groups_list, name='group_list'),
]
