# Generated by Django 3.2.3 on 2021-06-07 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20210607_0858'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='announcement_post',
            field=models.CharField(max_length=255, null=True, verbose_name='Анонс статьи'),
        ),
    ]