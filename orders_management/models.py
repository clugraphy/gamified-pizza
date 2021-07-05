from django.db import models
from django.db.models.fields.related import ForeignKey, OneToOneField
from django.contrib.auth.models import User

# Create your models here.
from orders.models import Product


class Order(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    nickname = models.CharField(max_length=40)
    email = models.EmailField()
    address = models.CharField(max_length=150)
    postal_code = models.CharField(max_length=30)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ("-created", "first_name", "last_name")

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    def get_total_pizzereum(self):
        return sum(item.get_pizzereum() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name="order_items", on_delete=models.CASCADE
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pizzereum = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return "OrderItem: {} pizzereum: {}".format(self.pk, self.pizzereum)

    def get_cost(self):
        return self.price * self.quantity

    def get_pizzereum(self):
        return self.pizzereum * self.quantity


class Leaderboard(models.Model):
    first_name = ForeignKey(
        Order,
        blank=True,
        null=True,
        related_name="userFirstID",
        on_delete=models.CASCADE,
    )
    last_name = ForeignKey(
        Order,
        blank=True,
        null=True,
        related_name="userLastID",
        on_delete=models.CASCADE,
    )
    order = ForeignKey(
        OrderItem,
        blank=True,
        null=True,
        related_name="orderID",
        on_delete=models.CASCADE,
    )
    pizzereum = ForeignKey(
        OrderItem,
        blank=True,
        null=True,
        related_name="pizzereums",
        on_delete=models.CASCADE,
    )
    quantity = OneToOneField(
        OrderItem, auto_created=True, default="", on_delete=models.CASCADE
    )

    def __str__(self):
        return "Leaderboard: {} {}".format(self.pizzereum, self.first_name)
