from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse


# Create your models here.

class Category(models.TextChoices):
    UNCATEGORISED = "UNCATEGORISED", "UnCategorized"


ORDER_STATUS = (
    ("CheckOut","CheckOut"),
    ("Placed", "Placed"),
    ("Processed", "Processed"),
    ("Delivered", "Delivered"),
    ("Completed", "Completed"),
)


class Banner(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="img/banners", default="bannerPH.jpg")


class Tag(models.Model):
    name = models.CharField(max_length=100)
    isActive = models.BooleanField(default=False)
    banner = models.ForeignKey(Banner, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=25)
    image = models.ImageField(upload_to="img/products", default="productPH.png")
    description = models.TextField()
    discount = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    category = models.CharField(max_length=50, choices=Category.choices, default=Category.UNCATEGORISED)
    tag = models.ManyToManyField(Tag)
    unit = models.CharField(max_length=50, default="Kgs")
    availability = models.BooleanField(default=True),
    section = models.CharField(max_length=100, default="ALL")
    recomPoints = models.IntegerField(default=0)
    dealPoints = models.IntegerField(default=0)
    deliveryPoints = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Review(models.Model):
    review = models.TextField()
    rating = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name


class UserToken(models.Model):
    token = models.CharField(max_length=1000)
    deviceId = models.CharField(max_length=500, primary_key=True)
    isActive = models.BooleanField(default=True)
    address = models.CharField(max_length=1000, default="", blank=True)
    phoneNumber = models.CharField(max_length=20, default="", blank=True)
    name = models.CharField(max_length=500, default="", blank=True)
    email = models.CharField(max_length=300, default="", blank=True)
    password = models.CharField(max_length=300, default="", blank=True)
    dateAdded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.deviceId


class Order(models.Model):
    identification = models.ForeignKey(UserToken, on_delete=models.CASCADE)
    price = models.IntegerField(default=0.0)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=ORDER_STATUS, default="CheckOut")
    items = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    contact = models.CharField(max_length=1000)
    contactName = models.CharField(max_length=1000)
    orderId = models.IntegerField(default=0)
    remoteOrderId = models.IntegerField(default=0)
    # paymentMode = models.CharField(max_length=50, )

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Order")

    def __str__(self):
        return self.contactName

    def get_absolute_url(self):
        return reverse("Order", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    class Meta:
        unique_together = ('order', 'product')


class District(models.Model):
    name = models.CharField(max_length=50)
    isActive = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("District")
        verbose_name_plural = _("District")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("District_detail", kwargs={"pk": self.pk})


class Division(models.Model):
    name = models.CharField(max_length=50)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    isActive = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Division")
        verbose_name_plural = _("Division")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Division_detail", kwargs={"pk": self.pk})


class Parish(models.Model):
    name = models.CharField(max_length=50)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    isActive = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("parish")
        verbose_name_plural = _("parish")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("parish_detail", kwargs={"pk": self.pk})


class Village(models.Model):
    name = models.CharField(max_length=50)
    parish = models.ForeignKey(Parish, on_delete=models.CASCADE)
    isActive = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("village")
        verbose_name_plural = _("village")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("village_detail", kwargs={"pk": self.pk})


class Street(models.Model):
    name = models.CharField(max_length=50)
    village = models.ForeignKey(Village, on_delete=models.CASCADE)
    isActive = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("street")
        verbose_name_plural = _("street")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("street_detail", kwargs={"pk": self.pk})
