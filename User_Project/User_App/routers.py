from rest_framework import routers
from User_App import views

router = routers.DefaultRouter ()

router.register ( 'User' , views.UserViewSet , basename='user' )