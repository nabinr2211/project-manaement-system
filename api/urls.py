from api import views
from django.urls import path

app_name = 'api'
urlpatterns = [
    # urls for program...
    path('program-list/', views.program_list, name='api_program_list'),
    # path('program-detail/<str:pk>/',views.program_detail_api,name='api_program_detail'),
    path('add-program/', views.program_add_api, name='api_program_add'),
    path('update-program/<str:pk>/', views.program_update_api, name='api_program_update'),

    # urls for members...

    path('add-member/', views.member_add_api, name='api_member_add'),
    path('member-list/', views.member_list_api, name='api_member_list'),
    path('member-detail/<str:pk>/',views.member_detail_api,name='api_member_detail'),
    path('update-member/<str:pk>/', views.member_update_api, name='api_member_update'),

]
