# Define here e models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from apps.kol import models as Kol
from apps.note import models as Note

class KolItem(DjangoItem):
    table = 'kol_info'
    django_model = Kol.Info

class NoteItem(DjangoItem):

    table= 'note_info'
    django_model = Note.Info

class DanmuItem(DjangoItem):
    table = 'note_danmu'
    django_model = Note.Danmu

class CommentItem(DjangoItem):

    table = 'note_comment'
    django_model = Note.Comment
