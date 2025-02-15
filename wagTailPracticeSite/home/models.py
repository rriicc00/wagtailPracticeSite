from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, PageChooserPanel
from wagtail.fields import RichTextField
from wagtail.images import get_image_model



class HomePage(Page):
    template = "home/home_page.html"
    max_count = 1

    subtitle = models.CharField(max_length=100, blank=True, null=True)
    body = RichTextField(blank=True)

    video_url = models.URLField(blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('body'),
        FieldPanel('video_url'),
    ]
    




