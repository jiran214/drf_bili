# Generated by Django 4.1.1 on 2022-09-23 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0011_alter_info_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_hotwords',
            name='aid',
            field=models.ForeignKey(db_column='aid', on_delete=django.db.models.deletion.CASCADE, related_name='comment_hotword', to='note.info', to_field='aid'),
        ),
    ]
