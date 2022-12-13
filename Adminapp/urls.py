from django.urls import path
from . import views
urlpatterns = [
    path('adminindex/',views.adminindex,name='adminindex'),
    path('addbranches/',views.addbranches,name='addbranches'),
    path('viewbranches/',views.viewbranches,name='viewbranches'),
    path('getData/',views.getData,name='getData'),
    path('delete/<int:did>/',views.delete,name='delete'),
    path('branch_edit/<int:did>/',views.branch_edit,name='branch_edit'),
    path('branchupdate/<int:did>/',views.branchupdate,name='branchupdate'),
    path('addservices/',views.addservices,name='addservices'),
    path('getDetails/',views.getDetails,name='getDetails'),
    path('viewservices/',views.viewservices,name='viewservices'),
    path('servicedelete/<int:did>/',views.servicedelete,name='servicedelete'),
    path('serviceedit/<int:did>/',views.serviceedit,name='serviceedit'),
    path('update/<int:did>/',views.update,name='update'),
    path('viewuser/',views.viewuser,name='viewuser'),
    path('viewappoinments/',views.viewappoinments,name='viewappoinments'),
    path('viewmessages/',views.viewmessages,name='viewmessages'),
    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('getAdmin/',views.getAdmin,name='getAdmin'),
    path('adminlogout/',views.adminlogout,name='adminlogout')
]


