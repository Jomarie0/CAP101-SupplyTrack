from django.db import models
from apps.suppliers.models import Supplier # Importing Supplier from suppliers app

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField(default=0)
    reorder_level = models.PositiveIntegerField(default=10)  # Alert when stock is low
    unit = models.CharField(max_length=50, default="pcs")  # Example: kg, liters, packs
    category = models.CharField(max_length=100, blank=True, null=True)  # Optional category
    created_at = models.DateTimeField(auto_now_add=True)  # Auto timestamp on creation
    updated_at = models.DateTimeField(auto_now=True)  # Auto update timestamp

    def __str__(self):
        return self.name

# class Supplier(models.Model):
#     name = models.CharField(max_length=255)
#     contact_person = models.CharField(max_length=255, blank=True, null=True)
#     email = models.EmailField(unique=True)
#     phone = models.CharField(max_length=15, blank=True, null=True)
#     address = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return self.name


class PurchaseOrder(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    expected_delivery = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=[("Pending", "Pending"), ("Completed", "Completed"), ("Canceled", "Canceled")],
        default="Pending"
    )

    def __str__(self):
        return f"Order {self.id} - {self.supplier.name}"


class StockMovement(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    movement_type = models.CharField(
        max_length=10,
        choices=[("IN", "Stock In"), ("OUT", "Stock Out")],
    )
    quantity = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.movement_type} - {self.product.name} ({self.quantity})"
