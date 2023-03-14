from django.contrib import admin
from django.urls import path
from . import views

app_name='todoprojectapp'
urlpatterns = [
    path('',views.add,name='add'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbv/',views.Tasklistview.as_view(),name='cbv'),
    path('cbvdetails/<int:pk>/',views.Taskdetailview.as_view(),name='cbvdetails'),
    path('cbvupdate/<int:pk>/',views.Taskupdate.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.Taskdeleteview.as_view(),name='cbvdelete'),
    # path('details',views.details,name='details')

]
