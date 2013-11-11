from django.db import models
from django.db.models import permalink
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    @permalink
    def get_absolute_url(self):
        return ('blog-category', None, { 'slug': self.slug })


class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return '%s' % self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    @permalink
    def get_absolute_url(self):
        return ('blog-post', None, { 'slug': self.slug })
