from wagtail.api.v2.views import BaseAPIViewSet, BaseSerializer
from .models import Menu


class MenuViewSet(BaseAPIViewSet):
    model = Menu
    body_fields = BaseAPIViewSet.body_fields + ['title', 'slug', 'menu_items']
    listing_default_fields = BaseAPIViewSet.listing_default_fields + \
        ['title', 'slug', 'menu_items']
