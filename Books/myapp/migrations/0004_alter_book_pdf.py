# Generated by Django 4.2.1 on 2023-06-01 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_book_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='pdf/'),
        ),
    ]
