# Generated by Django 5.1.7 on 2025-03-31 13:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
        ('suppliers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suppliers.supplier'),
        ),
        migrations.RenameField(
            model_name='product',
            old_name='stock',
            new_name='stock_quantity',
        ),
        migrations.AddField(
            model_name='product',
            name='reorder_level',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='product',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='suppliers.supplier'),
        ),
        migrations.AddField(
            model_name='product',
            name='unit',
            field=models.CharField(default='pcs', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.DeleteModel(
            name='Supplier',
        ),
    ]
