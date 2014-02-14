from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from markdown2 import Markdown
from BeautifulSoup import BeautifulSoup
from pretty_times import pretty
from taggit.managers import TaggableManager
from tildeslash.blog.utils import strip_content, word_count

markdowner = Markdown(extras=['fenced-code-blocks', ])


class Post(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    slug = models.CharField(max_length=255, null=False, blank=False, unique=True)
    author = models.ForeignKey(User, related_name='posts')
    content = models.TextField(blank=True, default='')
    publish_time = models.DateTimeField(default=datetime.now)
    status = models.CharField(max_length=20, null=False, default='draft', choices=(('draft', 'Draft'), ('published', 'Published')))
    tags = TaggableManager()

    @property
    def text_excerpt(self):
        return strip_content(self.text_content, 300)

    @property
    def word_count(self):
        return word_count(self.text_content)

    @property
    def text_content(self):
        return ''.join(BeautifulSoup(self.html_content).findAll(text=True))

    @property
    def html_content(self):
        return markdowner.convert(self.content)

    @property
    def publish_date_relative(self):
        return pretty.date(self.publish_time)