from rest_framework import routers

from mainapp.api.api_views import CategoryViewSet, ProductViewSet, CartViewSet


router = routers.SimpleRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'carts', CartViewSet)
urlpatterns = router.urls