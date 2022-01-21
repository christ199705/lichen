from django.db import models


# Create your models here.
class Style(models.Model):
    style_name = models.CharField("菜单类别名", max_length=50)


class Dishes(models.Model):
    dishes_name = models.CharField("菜名", max_length=50)
    comment = models.FloatField("好评度")
    img_link = models.ImageField("图片")
    stock = models.IntegerField("库存")
    price = models.FloatField("单价")
    volume = models.IntegerField("月销量")
    Style = models.ForeignKey(Style, on_delete=models.CASCADE)
