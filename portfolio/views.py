from wagtail.api.v2.views import PagesAPIViewSet
from django.urls import reverse, path

class CustomPagesAPIViewSet(PagesAPIViewSet):
    def detail_view(self, request, pk=None, slug=None):
        param = pk
        if slug is not None:
            self.lookup_field = 'slug'
            param = slug
        return super().detail_view(request, param)
    
    @classmethod
    def get_urlpatterns(cls):
        return [
            path('', cls.as_view({'get': 'listing_view'}), name='listing'),
            path('<int:pk>/', cls.as_view({'get': 'detail_view'}), name='detail'),
            path('<slug:slug>/', cls.as_view({'get': 'detail_view'}), name='detail'),
            path('find/', cls.as_view({'get': 'find_view'}), name='find'),
        ]