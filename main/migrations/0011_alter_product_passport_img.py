# Generated by Django 5.0.2 on 2024-04-22 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_rename_pasport_product_passport_pdf_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='passport_img',
            field=models.ImageField(blank=True, null=True, upload_to='products', verbose_name='Паспорт изображение'),
        ),
    ]