# Generated by Django 3.0.8 on 2020-09-16 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_order_user_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='points_earned',
            field=models.IntegerField(default=0),
        ),
    ]
