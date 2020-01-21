from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import OrderDetail


@receiver(post_save, sender=OrderDetail)
def update_order_total(sender, instance, **kwargs):
    order = instance.order
    if order.order_detail.count() > 0:
        order.total = order.order_detail.aggregate(total=models.Sum('line_total'))['total']
    else:
        order.total = 0
    order.save()