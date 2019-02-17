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
    path('api/categories/', views.categories_list, name='categories_list'),
    path('api/statuses/', views.statuses_list, name='statuses_list'),
    path('api/groups/', views.groups_list, name='group_list'),
    path('api/uploadimage/', views.FileUploadView.as_view(), name='upload_image')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# all points between square
