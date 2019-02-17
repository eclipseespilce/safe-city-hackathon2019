from django.urls import path
from mapApi import views
from django.conf.urls import url
from django.conf.urls.static import static

from OpenMap import settings


app_name = 'mapApi'

urlpatterns = [
    path('api/points/', views.add_point, name='add_point'),
    path('api/points/<str:groupId>', views.points_by_group, name='points_by_group'),
    path('api/allpoints/', views.all_points, name='all_points'),
    path('api/groups/', views.groups_list, name='group_list'),
    path('api/uploadimage/', views.upload_image, name='upload_image')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# all points between square