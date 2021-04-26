from projects import views
from django.urls import path

# assign app name
app_name = 'projects'
urlpatterns = [
    path('add-program/', views.add_program, name='add_program'),
    path('program-list/', views.program_list, name='program_list'),
    path('edit-program/<int:id>', views.edit_program, name="edit_program"),
    path('delete-program/<int:id>', views.delete_program, name="delete_program"),

    path('add-member/', views.add_member, name='add_member'),
    path('member-list/', views.member_list, name='member_list'),
    path('edit-member/<int:id>', views.edit_member, name="edit_member"),
    path('delete-member/<int:id>', views.delete_member, name="delete_member"),

    path('add-supervisor/', views.add_supervisor, name='add_supervisor'),
    path('supervisor-list/', views.supervisor_list, name='supervisor_list'),
    path('edit-supervisor/<int:id>', views.edit_supervisor, name="edit_supervisor"),
    path('delete-supervisor/<int:id>', views.delete_supervisor, name="delete_supervisor"),

    path('add-task/', views.add_task, name='add_task'),
    path('task-list/', views.task_list, name='task_list'),
    path('edit-task/<int:id>', views.edit_task, name="edit_task"),
    path('delete-task/<int:id>', views.delete_task, name="delete_task"),

    path('add-project/', views.add_project, name='add_project'),
    path('project-list/', views.project_list, name='project_list'),
    path('edit-project/<int:id>', views.edit_project, name="edit_project"),
    path('delete-project/<int:id>', views.delete_project, name="delete_project"),
    path('project/<int:pk>', views.ProjectDetails.as_view(), name='project_details'),

    path('user/login/', views.user_login, name='user_login'),
    path('user/logout/', views.user_logout, name='user_logout'),

]
