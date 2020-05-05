from wagtail.api.v2.views import PagesAPIViewSet
from wagtail.api.v2.router import WagtailAPIRouter
from wagtail.images.api.v2.views import ImagesAPIViewSet
from wagtail.documents.api.v2.views import DocumentsAPIViewSet
from .views import CustomPagesAPIViewSet
from menu.views import MenuViewSet

api_router = WagtailAPIRouter('wagtailapi')

api_router.register_endpoint('pages', CustomPagesAPIViewSet)
api_router.register_endpoint('images', ImagesAPIViewSet)
api_router.register_endpoint('documents', DocumentsAPIViewSet)
api_router.register_endpoint('menus', MenuViewSet)
