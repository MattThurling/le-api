# Generated by Django 5.1.7 on 2025-03-10 13:56

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_page_image_alter_page_video_alter_post_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]
