from django.db import models
from embed_video.fields import EmbedVideoField


# Create your models here.
class Slide(models.Model):
    background_image = models.ImageField(upload_to='slides/')
    caption_heading = models.CharField(max_length=255)
    caption_subheading = models.CharField(max_length=255)
    button_text = models.CharField(max_length=50)
    button_link = models.URLField()

    def __str__(self):
        return self.caption_heading
    

class FeaturedEvent(models.Model):
    parallax_image = models.ImageField(upload_to='events/')
    event_date = models.DateField()
    event_location = models.CharField(max_length=255)
    event_title = models.CharField(max_length=255)
    countdown_time = models.DateTimeField()
    event_image = models.ImageField(upload_to='events/')
    button_text = models.CharField(max_length=50)
    button_link = models.URLField()

    def __str__(self):
        return self.event_title
    
class Video(models.Model):
    title = models.CharField(max_length=255)
    # youtube_url = models.URLField()
    youtube_url = EmbedVideoField()
    thumbnail_image = models.ImageField(upload_to='thumbnails/')
    thumbnail_alt = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title
    

class GalleryItem(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    original_image = models.ImageField(upload_to='gallery/originals/')
    thumbnail_image = models.ImageField(upload_to='gallery/thumbnails/')

    def __str__(self):
        return self.title
    
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    image = models.ImageField(upload_to='blog/images/')
    content = models.TextField(null=True)
    # excerpt = models.TextField()
    # link = models.URLField()

    def __str__(self):
        return self.title
    

class Event(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    location = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255, default='TZA')

    def __str__(self):
        return self.title
    

class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='service/images/')
    # excerpt = models.TextField()
    # link = models.URLField()

    def __str__(self):
        return self.title