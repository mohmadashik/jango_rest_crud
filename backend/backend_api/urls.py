from .views import StudentViewSet
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'students',views.StudentViewSet,basename='student')
urlpatterns = router.urls
print(urlpatterns,'*******urlpatterns***********')