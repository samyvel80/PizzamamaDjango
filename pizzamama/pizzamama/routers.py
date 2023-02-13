from rest_framework.routers import DefaultRouter
from menu.views import PizzaViewset

router = DefaultRouter()
router.register('api', PizzaViewset, basename='producta')
print(router.urls)
urlpatterns = router.urls



#router.register('ListRetrieve', ProductListRetrieveViewset, basename='ListRetrieve')