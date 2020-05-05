from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, RichTextFieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.documents.edit_handlers import DocumentChooserPanel

from modelcluster.fields import ParentalKey


class Work(Orderable, models.Model):
    page = ParentalKey('WorksPage', on_delete=models.CASCADE,
                       related_name='works')
    image = models.ForeignKey('wagtailimages.Image', null=True,
                              blank=True, on_delete=models.SET_NULL, related_name='+')
    name = models.CharField(blank=True, max_length=70)
    description = RichTextField(blank=True)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('name'),
        RichTextFieldPanel('description'),
    ]

    api_fields = ['image', 'name', 'description']


class SocialIcon(Orderable, models.Model):
    page = ParentalKey('AboutPage', on_delete=models.CASCADE,
                       related_name='social_icons')
    name = models.CharField(max_length=15)
    icon = models.CharField(max_length=15)
    link = models.CharField(max_length=50, default='#')

    api_fields = ['icon', 'link']


class HomePage(Page):
    featured_title = models.CharField(max_length=50)
    tagline = models.CharField(max_length=50)

    content_panels = Page.content_panels + [
        FieldPanel('featured_title', classname='full'),
        FieldPanel('tagline', classname='full'),
    ]

    api_fields = ['featured_title', 'tagline']


class AboutPage(Page):
    picture = models.ForeignKey('wagtailimages.Image', null=True,
                                blank=True, on_delete=models.SET_NULL, related_name='+')
    presentation = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel('picture'),
        InlinePanel('social_icons', label='Social Icons'),
        RichTextFieldPanel('presentation', classname='full'),
    ]

    api_fields = ['picture', 'presentation', 'social_icons']


class WorksPage(Page):
    content_panels = Page.content_panels + [
        InlinePanel('works', label='Works'),
    ]

    api_fields = ['works']