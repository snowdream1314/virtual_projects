# from django.db import models

from mongoengine import *
from mysite.settings import DBNAME


# from mongoengine import connect
# Create your models here.
connect('smzdm_fx_item', host='localhost', port=27017)

# class smzdm_fx(Document):
#     itemid = Item.itemid
#     categoryid = Item.categoryid
#     name = Item.name
#     image = Item.image
#     href = Item.href
#     brandname = Item.brandname
#     price = Item.price
#     originprice = Item.originprice
#     updatetime = Item.updatetime
#     bad_count = IntField()
#     
#     def createItemdic(self, dict2):
#         return Item.createItemdic(self, dict2)

class smzdm_fx_item(Document):
    itemid = IntField()
    categoryid = IntField()
    name = StringField()
    image = StringField()
    href = StringField()
    brandname = StringField()
    price = StringField()
    originprice = StringField()
    updatetime = IntField()
    bad_count = IntField()
    originmall = StringField()
    # originmallurl = StringField()
    comment_count = IntField()
    good_count = IntField()
    fav_count = IntField()
    article_time = StringField()
    article_url = StringField()
    item_description = StringField(max_length=30)
    youhui_content = StringField(max_length=30)
    baoliao_content = StringField(max_length=30)
    


