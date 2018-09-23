from django.conf.urls import url, include
from django.contrib import admin

# from api import views
from v2 import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

router = routers.DefaultRouter()
router.register('catalogs',views.CatalogView)
router.register('companies',views.CompanyView)
router.register('users',views.UserView)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include(router.urls)),
]
