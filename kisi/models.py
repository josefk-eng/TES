from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _


# Create your models here.

class KProduct(models.Model):
    name = models.CharField(max_length=100, default="name")
    image = models.CharField(max_length=1000, default="", blank=True)
    price = models.CharField(max_length=100, default="0.00")
    rating = models.IntegerField(default=0)
    type = models.CharField(max_length=20, default="Cake")
    tag = models.CharField(max_length=1000, default="All,")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("KProduct_detail", kwargs={"pk": self.pk})


class KReview(models.Model):
    text = models.CharField(max_length=1000, default="")
    rate = models.IntegerField(default=0)
    product = models.ForeignKey(KProduct, on_delete=models.CASCADE, default=1)
    date = models.FloatField()
    owner = models.CharField(max_length=1000, default="")

    class Meta:
        verbose_name = _("KReview")
        verbose_name_plural = _("KReview")

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse("KReview_detail", kwargs={"pk": self.pk})
