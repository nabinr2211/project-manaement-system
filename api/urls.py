from api import views
from django.urls import path

app_name = 'api'
urlpatterns = [

    # urls for program...
    path('program-list/', views.program_list, name='api_program_list'),
    # path('program-detail/<str:pk>/',views.program_detail_api,name='api_program_detail'),
    path('add-program/', views.program_add_api, name='api_program_add'),
    path('update-program/<str:pk>/', views.program_update_api, name='api_program_update'),
    path('delete-program/<str:pk>/', views.delete_program_api, name='delete_program_api'),

    # urls for members...
    path('add-member/', views.member_add_api, name='api_member_add'),
    path('member-list/', views.member_list_api, name='api_member_list'),
    path('member-detail/<str:pk>/', views.member_detail_api, name='api_member_detail'),
    path('update-member/<str:pk>/', views.member_update_api, name='api_member_update'),

    # urls for supervisor...
    path('add-supervisor/', views.supervisor_add_api, name='api_supervisor_add'),
    path('supervisor-list/', views.supervisor_list_api, name='api_supervisor_list'),
    path('supervisor-detail/<str:pk>/', views.supervisor_detail_api, name='api_supervisor_detail'),
    path('update-supervisor/<str:pk>/', views.supervisor_update_api, name='api_supervisor_update'),

    # urls for task...
    path('add-task/', views.task_add_api, name='api_task_add'),
    path('task-list/', views.task_list_api, name='api_task_list'),
    path('task-detail/<str:pk>/', views.task_detail_api, name='api_task_detail'),
    path('update-task/<str:pk>/', views.task_update_api, name='api_task_update'),

    # urls for project...
    path('add-project/', views.project_add_api, name='api_project_add'),
    path('project-list/', views.project_list_api, name='api_project_list'),
    path('project-detail/<str:pk>/', views.project_detail_api, name='api_project_detail'),
    path('update-project/<str:pk>/', views.project_update_api, name='api_project_update'),

]
