from django.conf import settings
from django.db import models

class FoodCategory(models.Model):
    ''' Food Category model '''

    class Meta:
        verbose_name_plural = "Food Categories"
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Food(models.Model):
    ''' Food model '''
    name = models.CharField(max_length=256)
    food_type = models.ForeignKey(FoodCategory, on_delete=models.PROTECT)
    price = models.FloatField(default='1.50')

    def __str__(self):
        return self.name


class Order(models.Model):
    ''' Order header model '''
    CART = 'T'
    NEW = 'N'
    SENT = 'S'
    RECEIVED = 'R'
    CANCELLED = 'C'
    STATUS_CHOICES = [
        (CART, 'Cart'),
        (NEW, 'New'),
        (SENT, 'Sent'),
        (RECEIVED, 'Received'),
        (CANCELLED, 'Cancelled'),
    ]
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT)
    status = models.CharField(
        max_length=32,
        choices=STATUS_CHOICES,
        default=NEW)
    total = models.FloatField(default='0.00')
    created = models.DateTimeField(null=True, blank=True)

    def calculate_totals(self):
        ''' recalculates all line totals and order total '''
        self.total = 0
        self.order_detail.update(
            line_total=models.F('quantity')*models.F('unit_price'))
        self.total = self.order_detail.aggregate(
            total=models.Sum('line_total'))['total']


class OrderDetail(models.Model):
    ''' Order detail model '''
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='order_detail')
    food = models.ForeignKey(Food, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=0)
    unit_price = models.FloatField(default='1.50')
    line_total = models.FloatField(default='1.50')
