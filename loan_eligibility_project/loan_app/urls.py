from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('loan_app', views.ApprovalsViews)

urlpatterns = [
    path('', views.usercontact, name='userform'),
    path('app/', include(router.urls)),
    path('status/', views.approvereject),
]
