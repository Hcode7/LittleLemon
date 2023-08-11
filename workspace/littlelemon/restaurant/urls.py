from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

from .views import UserViewSet
user_list_view = UserViewSet.as_view({
    'get': 'list',  # Allow the 'list' action (GET request)
})


urlpatterns = [
    path('', views.index, name='home'),
    path('items/', views.MenuItemView.as_view()),
    path('items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('users/', user_list_view, name='user-list'),
    path('api-token-auth/', obtain_auth_token)
]