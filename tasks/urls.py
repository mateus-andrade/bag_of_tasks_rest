
from rest_framework import routers
from .views import TaskViewSet

router = routers.DefaultRouter()
router.register(r'', TaskViewSet, base_name='task')
urlpatterns = router.urls
