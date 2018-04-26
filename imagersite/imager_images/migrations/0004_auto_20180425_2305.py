# Generated by Django 2.0.4 on 2018-04-25 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0003_remove_photo_album'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='published',
            field=models.CharField(choices=[('PRIVATE', 'Private'), ('SHARED', 'Shared'), ('PUBLIC', 'Public')], max_length=12),
        ),
        migrations.AlterField(
            model_name='photo',
            name='published',
            field=models.CharField(choices=[('PRIVATE', 'Private'), ('SHARED', 'Shared'), ('PUBLIC', 'Public')], max_length=12),
        ),
    ]