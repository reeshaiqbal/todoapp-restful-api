from rest_framework import routers
from .views import TodoViewSet

# create url's here

router = routers.DefaultRouter()
# Registering the TodoViewSet with the router
router.register(r'todos', TodoViewSet, basename='todo')
urlpatterns = router.urls
