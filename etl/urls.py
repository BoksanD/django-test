from django.urls import path
from . import views



urlpatterns = [
    path('launch/', views.LaunchUtilityView.as_view(), name='launch-utility'),
    # Clients
    path('clients/',views.ClientListView.as_view(), name='client-list'),    
    path('clients/add/',views.ClientCreateView.as_view(), name='client-add'),
    path('clients/<int:pk>/edit/',views.ClientUpdateView.as_view(), name='client-edit'),
    path('clients/<int:pk>/delete/',views.ClientDeleteView.as_view(),name='client-delete'),
    # Insurences
    path('insurences/', views.InsurenceListView.as_view(),name='insurence-list'),
    path('insurences/add/', views.InsurenceCreateView.as_view(),name='insurence-add'),
    path('insurences/<int:pk>/edit',views.InsurenceUpdateView.as_view(),name='insurence-edit'),
    path('insurences/<int:pk>/delete', views.InsurenceDeleteView.as_view(),name='insurence-delete'),
    # Subscriptions
    path('subscriptions/',views.SubscriptionListView.as_view(),name='subscription-list'),
    path('subscriptions/add/',views.SubscriptionCreateView.as_view(),name='subscription-add'),
    path('subscriptions/<int:pk>/edit/',views.SubscriptionUpdateView.as_view(),name='subscription-edit'),
    path('subscriptions/<int:pk>/delete/',views.SubscriptionDeleteView.as_view(),name='subscription-delete'),

    # Payments
    path('payments/add/<int:subscription_id>/', views.PaymentCreateView.as_view(), name='payment-add'),
    path('payments/list/<int:subscription_id>/', views.PaymentListView.as_view(), name='payment-list'),

    # Etl Source System
    path('source-system/',views.SourceSystemView.as_view(), name='source-system-list'),    
    path('source-system/add',views.SourceSystemCreateView.as_view(), name='source-system-add'),    
]
