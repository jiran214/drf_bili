# Generated by Django 4.1.1 on 2022-09-15 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0004_alter_info_pub_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='danmu',
            name='ctime',
            field=models.CharField(max_length=10, verbose_name='发布时间'),
        ),
    ]