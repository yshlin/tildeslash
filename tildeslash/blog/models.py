from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from markdown2 import Markdown
from BeautifulSoup import BeautifulSoup

markdowner = Markdown(extras=['fenced-code-blocks', ])


class Post(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    slug = models.CharField(max_length=255, null=False, blank=False, unique=True)
    author = models.ForeignKey(User, related_name='posts')
    content = models.TextField(blank=True, default='')
    publish_time = models.DateTimeField(default=datetime.now)
    status = models.CharField(max_length=20, null=False, default='draft', choices=(('draft', 'Draft'), ('published', 'Published')))

    @property
    def text_content(self):
        return ''.join(BeautifulSoup(self.html_content).findAll(text=True))

    @property
    def html_content(self):
        return markdowner.convert(self.content)
