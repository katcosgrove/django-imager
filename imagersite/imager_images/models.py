from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField
from django.dispatch import receiver
from django.utils import timezone


class Photo(models.Model):
    """Photo class for album photos."""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='photos')
    image = ImageField(upload_to='images')
    title = models.CharField(max_length=180, default='Untitled')
    description = models.TextField(blank=True, null=True)
    date_uploaded = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    date_published = models.DateField(blank=True, null=True)
    published = models.CharField(
        max_length=100,
        choices=(
            ('PRIVATE', 'Private'),
            ('SHARED', 'Shared'),
            ('PUBLIC', 'Public'),
        )
    )

    def __str__(self):
        """Return the title of the photo."""
        return '{}'.format(self.title)


class Album(models.Model):
    """Create album objects."""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='albums')
    cover = models.ForeignKey('Photo', on_delete=models.CASCADE, related_name='+', null=True, blank=True)
    photos = models.ManyToManyField(Photo, related_name='album')
    title = models.CharField(max_length=180, default='Untitled')
    description = models.TextField(blank=True, null=True)
    date_uploaded = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    date_published = models.DateField(blank=True, null=True)
    published = models.CharField(
        max_length=100,
        choices=(
            ('PRIVATE', 'Private'),
            ('SHARED', 'Shared'),
            ('PUBLIC', 'Public'),
        )
    )

    def __str__(self):
        """Return the title of the album."""
        return '{}'.format(self.title)


@receiver(models.signals.post_save, sender=Photo)
def set_photo_date_published(sender, instance, **kwargs):
    if instance.published == 'PUBLIC' and not instance.date_published:
        instance.date_published = timezone.now()

    
@receiver(models.signals.post_save, sender=Album)
def set_album_date_published(sender, instance, **kwargs):
    if instance.published == 'PUBLIC' and not instance.date_published:
        instance.date_published = timezone.now()