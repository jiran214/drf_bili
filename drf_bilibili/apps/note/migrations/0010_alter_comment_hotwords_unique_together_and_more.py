# Generated by Django 4.1.1 on 2022-09-16 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0009_alter_danmu_hotwords_cid'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='comment_hotwords',
            unique_together={('aid', 'hot_word')},
        ),
        migrations.AlterUniqueTogether(
            name='danmu_hotwords',
            unique_together={('cid', 'hot_word')},
        ),
    ]