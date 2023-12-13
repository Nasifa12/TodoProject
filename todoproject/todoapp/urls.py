from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.add, name='add'),
    path('cbvdetail/<int:pk>', views.TaskDetailview.as_view(), name='cbvdetail'),
    path('delete/<int:taskid>', views.delete, name='delete'),
    path('update/<int:taskid>', views.update, name='update'),
    path('cbvhome/', views.Tasklistview.as_view(), name='cbvhome'),
    path('cbvupdate/<int:pk>', views.TaskUpdateview.as_view(), name='cbvpdate'),
    path('cbvdelete/<int:pk>', views.TaskDeleteView.as_view(), name='cbvdelete'),

]
