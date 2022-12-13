from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('login/',views.login,name='login'),
    path('branches/',views.branches,name='branches'),
    path('services/',views.services,name='services'),
    path('getValue/',views.getValue,name='getValue'),
    path('registration/',views.registration,name='registration'),
    path('getRegister/',views.getRegister,name='getRegister'),
    path('getLogin/',views.getLogin,name='getLogin'),
    path('productdetails/',views.productdetails,name='productdetails'),
    path('viewdetails/<str:branchname>/',views.viewdetails,name='viewdetails'),
    path('getCart/',views.getCart,name='getCart'),
    path('logout/',views.logout,name='logout'),
    path('getBooking/',views.getBooking,name='getBooking'),
    path('cartdelete/<int:did>/',views.cartdelete,name='cartdelete')
    


]