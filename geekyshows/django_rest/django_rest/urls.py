from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
#Creating Router Object
router= DefaultRouter()
router.register('studentapi', views.StudentModelViewSet,basename='api-root')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls')),
    path('gettoken/',obtain_auth_token)
    # path('studentapi/',views.listcreate.as_view()),
    # path('studentapi/<int:pk>/',views.retrieveupdateDestroy.as_view())
]
