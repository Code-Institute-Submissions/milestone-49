# Generated by Django 3.0.8 on 2020-09-14 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20200914_0256'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description_full',
            field=models.TextField(blank=True, null=True),
        ),
    ]
