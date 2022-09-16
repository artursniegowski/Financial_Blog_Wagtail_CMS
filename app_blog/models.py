from django import forms
from django.db import models

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.search import index
from wagtail.snippets.models import register_snippet

# template fot the blog
class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [ 
        FieldPanel('intro'),
    ]

    # modify the queryset of the blogindex page
    # make sure we only display published order
    # changing the order in which it is displayed
    def get_context(self, request, *args, **kwargs):
        context =  super().get_context(request, *args, **kwargs)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        return context


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE,
    )

# template for our blog post
class BlogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    categories = ParentalManyToManyField('app_blog.BlogCategory',blank=True)
    author = models.ForeignKey(
        'Profile',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # returns the image from the first gallery item (or None if no gallery items exist)
    def main_image(self):
        gallery_item_main = self.gallery_images.first()
        if gallery_item_main:
            return gallery_item_main.image
        else:
            return None

    content_panels = Page.content_panels + [ 
        MultiFieldPanel([ 
            FieldPanel('date'),
            FieldPanel('tags'),
            FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
            FieldPanel('author'),
        ], heading="Blog information"),
        FieldPanel('intro'),
        FieldPanel('body'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]

    search_fields = Page.search_fields + [ 
        index.SearchField('intro'),
        index.SearchField('body'),
    ]


class BlogPageGalleryImage(Orderable):
    page = ParentalKey(BlogPage, 
                        on_delete=models.CASCADE,
                        related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.CASCADE,
        related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [ 
        FieldPanel('image'),
        FieldPanel('caption'),
    ]


class BlogTagIndexPage(Page):

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        # filter by tag
        tag = request.GET.get('tag')
        blogpages = BlogPage.objects.filter(tags__name=tag)

        # updating the context
        context['blogpages'] = blogpages

        return context

@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [ 
        FieldPanel('name'),
        FieldPanel('icon'),
    ] 

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'blog categories'


@register_snippet
class Profile(models.Model):
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+'
    )
    
    panels = [ 
        FieldPanel('username'),
        FieldPanel('first_name'),
        FieldPanel('last_name'),
        FieldPanel('image'),
    ] 

    def __str__(self) -> str:
        return self.username

    class Meta:
            verbose_name = "Profiles-edit"