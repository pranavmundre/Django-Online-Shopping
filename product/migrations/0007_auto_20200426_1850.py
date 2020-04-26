# Generated by Django 3.0.5 on 2020-04-26 13:20

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20200426_1814'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(blank=True, max_length=155)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='allow_variants',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(blank=True, max_length=155)),
                ('price', models.DecimalField(decimal_places=2, max_digits=25)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
                ('variant', models.ManyToManyField(to='product.Attribute')),
            ],
        ),
        migrations.AddField(
            model_name='attribute',
            name='attribute_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='product.Variant'),
        ),
        migrations.AddField(
            model_name='attribute',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_attributes',
            field=models.ManyToManyField(related_name='product_attribute', to='product.Attribute'),
        ),
    ]
