# Generated by Django 5.1.6 on 2025-02-15 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_body_homepage_subtitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='video_url',
            field=models.URLField(blank=True, verbose_name='https://www.youtube.com/watch?v=UbnX6mWLTdY&ab_channel=Wagtail'),
        ),
    ]
