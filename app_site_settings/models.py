from django.db import models
from wagtail.contrib.settings.models import (
    BaseSiteSetting,
    register_setting,
)

@register_setting
class SiteSpecificSocialMediaSettings(BaseSiteSetting):
    instagram = models.URLField(max_length=100, blank=True)
    facebook = models.URLField(max_length=100, blank=True)
    twitter = models.URLField(max_length=100, blank=True)
    
    class Meta:
        verbose_name = "Site-specific social media settings"

