# Generated by Django 3.1.7 on 2022-03-09 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_cafe_management', '0002_products_dues'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dues',
            name='last_purchase_date',
        ),
        migrations.AlterField(
            model_name='dues',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
