from django.db import models

from wagtail.models import Page


class HomePage(Page):
    pass


from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.images.models import Image

class LandingPage(Page):
    page_title = models.CharField(max_length=255)
    content = RichTextField(blank=True)
    image = models.ForeignKey(
        Image,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('page_title'),
        FieldPanel('content'),
        FieldPanel('image'),
    ]

class Plant(models.Model):
    name = models.CharField(max_length=255)
    description = RichTextField(blank=True)
    location = models.CharField(max_length=255)
    image_url = models.URLField(null=True, blank=True)

    panels = [
        FieldPanel('name'),
        FieldPanel('description'),
        FieldPanel('location'),
        FieldPanel('image_url'),
    ]

    def __str__(self):
        return self.name
    
    