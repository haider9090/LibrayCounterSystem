from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.login_page, name='login'),
    path('signup/', views.sign_page, name='signup'),
    path('register/', views.register,name='register'),
    # path('validation/',views.validation, name='validation'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('reports/', views.reports, name='reports'),
    path('setting/', views.setting, name='setting'),
    path('assistant/', views.assistant, name='assistant'),
    path('add-user/', views.user_page, name='add-user'),
    path('register-user', views.addUser, name='register-user'),
    path('visitors/', views.visitors, name='visitors'),
    path('user', views.assistant, name='user'),
    path('delete-user/<int:id>/', views.delete_data, name='delete-user'),
    path('updata-data/<user_id>/', views.update_data, name='update-data'),
    path('save-edit-user', views.save_edit_user, name='save-edit-user'),

]
