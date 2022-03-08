# Generated by Django 4.0.2 on 2022-03-05 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_cafe_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('prod_id', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Product ID')),
                ('item_name', models.CharField(max_length=40, verbose_name='Product Name')),
                ('availabilty', models.IntegerField(default=0, verbose_name='Availability')),
                ('price', models.FloatField(verbose_name='Price')),
            ],
        ),
        migrations.CreateModel(
            name='Dues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('due', models.FloatField(verbose_name='Amount Due')),
                ('last_purchase_date', models.DateTimeField(verbose_name='Date of Last Purchase')),
                ('cus_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_cafe_management.customers', verbose_name='ID number')),
            ],
        ),
    ]
