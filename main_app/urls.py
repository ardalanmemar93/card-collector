from  django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cards/', views.cards_index, name='index'),
    path('cards/<int:card_id>/', views.cards_detail, name='detail'),
    path('cards/create/', views.CardCreate.as_view(), name='cards_create'),
    path('cards/<int:pk>/update/', views.CardUpdate.as_view(), name='cards_update'),
    path('cards/<int:pk>/delete/', views.CardDelete.as_view(), name='cards_delete'),
    path('cards/<int:card_id>/add_apraisal/', views.add_apraisal, name='add_apraisal'),
    path('cards/<int:card_id>/add_photo/', views.add_photo, name='add_photo'),
    path('cards/<int:card_id>/assoc_merch/<int:merch_id>/', views.assoc_merch, name='assoc_merch'),
    path('cards/<int:card_id>/unassoc_merch/<int:merch_id>/', views.unassoc_merch, name='unassoc_merch'),
    path('merchen/', views.MerchList.as_view(), name='merchen_index'),
    path('merchen/<int:pk>/', views.MerchDetail.as_view(), name='merchen_detail'),
    path('merchen/create/', views.MerchCreate.as_view(), name='merchen_create'),
    path('merchen/<int:pk>/update/', views.MerchUpdate.as_view(), name='merchen_update'),
    path('merchen/<int:pk>/delete/', views.MerchDelete.as_view(), name='merchen_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]