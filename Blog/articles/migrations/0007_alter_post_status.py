# Generated by Django 3.2.3 on 2021-06-09 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_alter_post_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(max_length=16, null=True, verbose_name='Статус статьи'),
        ),
    ]
