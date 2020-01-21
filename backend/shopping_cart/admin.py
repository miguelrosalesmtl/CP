from django.contrib import admin
from .models import (
    FoodCategory,
    Food,
    Order,
    OrderDetail)

class OrderDetailInline(admin.TabularInline):
    model = OrderDetail
    extra = 0


@admin.register(Order)
class OrderModel(admin.ModelAdmin):
    inlines = [
        OrderDetailInline,
    ]
    list_display = ['id', 'status']
    list_filter = ['status']


@admin.register(Food)
class FoodModel(admin.ModelAdmin):
    list_display = ['name', 'food_type', 'price']

@admin.register(FoodCategory)
class FoodCategoryModel(admin.ModelAdmin):
    list_display = ['name']
