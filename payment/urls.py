from django.urls import path
from . import views

urlpatterns = [
    path('payment_succsess/', views.payment_succsess, name='payment_succsess'),
    path('checkout/', views.checkout, name='checkout'),
    path('confirm_order/', views.confirm_order, name='confirm_order'),
    path('process_order/', views.process_order, name='process_order'),

]
